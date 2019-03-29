##### belajar pip install flask flask_cors flask_mysqldb
##flask_cors kayak postman
namab=input('Masukkan nama Anda: ')
kotab=input('Masukkan kota Anda: ')

import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='purwadhika'
)
kursor=db.cursor()
query='insert into orangx (nama) values (%s)'
val=namab,
kursor.execute(query,val)
db.commit()
kursora=db.cursor()
query='select id from orangx'
kursora.execute(query)
#print(kursora.fetchall())
dataor=kursora.fetchall()
dataora=dataor[len(dataor)-1][0]
print(dataora)
query='select * from kotax'
kursora.execute(query)
datako=kursora.fetchall()
kons=len(datako)
print(kons)
c=len(datako)+1 #bilangan selain id pada table kota
for i in range(len(datako)): #mencari apakah kota baru tesedia di table
    if kotab==datako[i][1]:
        kons=i
        c=i
        print(kons)
if c==len(datako)+1: #jika kota belum tersedia
    query='insert into kotax (nama) values(%s)'
    val=kotab,
    kursora.execute(query,val)
    db.commit()
    query='insert into orangkotax values(%s,%s)'
    val=dataora,len(datako)+1 #nomor id perlu ditambah satu karena bukan nomor index
    kursora.execute(query,val)
    db.commit()
if kons==c: #jika kota sudah tesedia
    query='insert into orangkotax values(%s,%s)'
    val=dataora,datako[kons][0]
    kursora.execute(query,val)
    db.commit()
query='select o.id,o.nama,k.id as id_kota,k.nama as nama_kota from orangx o, kotax k, orangkotax where o.id=orangkotax.id_orang and k.id=orangkotax.id_kota'
kursor.execute(query)    
#print(kursor.fetchall())
alldata=kursor.fetchall()
for i in range(len(alldata)):
    print(alldata[i])
