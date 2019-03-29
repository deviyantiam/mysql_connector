##pip install MySQL-connector-python

# nama='Andi'
# usia=34
# print('Halo %s! Usia Anda %d th.' % (nama,usia))


##PAKAI fetchall kalau print
import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234'
)
##Kursor=pointer yang ada di database
kursor=db.cursor()
kursor.execute('show databases')
##print(kursor.fetchall())
alldata=kursor.fetchall()
for i in range (0,len(alldata)):
   print(alldata[i][0]) #tuple
##kursor.execute('create database tes')
# print(kursor)

##kalau mau execute selain select, pakai commit

import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='tes'
)

'''
#cara matiin single quotation mark, pake \ jadi \'hai\' atau pake double quotation mark
kursor=db.cursor()
kursor.execute('create table testable (id int not null auto_increment, nama varchar(50) default \'Anonim\',primary key(id))')
#print(kursor.fetchall())
'''

kursor=db.cursor()
query='insert into testable (nama) values("Budi"),("Caca"),("Deni"),("Fafa")' #%s passing string
#val=("Andi") #error yang benar ("Andi",)
kursor.execute(query) #(query,nama)
db.commit()

#==================================================================
kursor=db.cursor()
query='insert into testable (nama,usia) values(%s,%s)'
val=("Andi",23)
kursor.execute(query,val) #executemany
db.commit() #masukkin data

#==================================================================
kursor=db.cursor()
query='insert into testable (nama,usia) values(%s,%s)'
val=('Ida',24),('Yanwar',25),('Aat',26) #bisa pakai [('Ida',24),('Yanwar',25),('Aat',26)]
kursor.executemany(query,val) #lebih dr 1 row
db.commit() 
#print(kursor.rowcount,'Data sukses tersimpan') #untuk kasih tau berapa data tersimpan pada command ini

#==================================================================
kursor=db.cursor()
query='select * from testable'
kursor.execute(query) 
hasil=kursor.fetchall()

for data in hasil:
    print(data[1],data[2])

#==================================================================
# kursor=db.cursor()
# query='delete from testable where id=%s'
# val=(2,) #harus set yang pakai koma
# kursor.execute(query,val)
# db.commit() 
# print(kursor.rowcount,'Data sukses terhapus')

#==================================================================
kursor=db.cursor()
query='insert into testable(nama,usia) values(%s,%s)'
val="Aat",3
kursor.execute(query,val)
db.commit() 
#print(kursor.rowcount,'Data sukses tersimpan')

#==================================================================
kursor=db.cursor()
query='update testable set usia=%s where id=%s'
val=(22,6),(22,7),(24,8)
kursor.executemany(query,val)
db.commit() 
# print(kursor.rowcount,'Data sukses tersimpan')

#==================================================================
# import mysql.connector
# db=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='1234',
#     database='purwadhika'
# )
# kursor=db.cursor()
# query='select o.id,o.nama,k.id as id_kota,k.nama as nama_kota from orangx o, kotax k, orangkotax where o.id=orangkotax.id_orang and k.id=orangkotax.id_kota'
# kursor.execute(query)
# print(kursor.fetchall()) #fetchone row pertama