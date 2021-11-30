import  pymysql
x=pymysql.connect(host='localhost',user='root',password='asdlab',db='rk')
cur=x.cursor()

#cur.execute('create table sample1(name char(50),place char(50),age int)')
print('------DATA SET--------------')
cur.execute('select * from sample1')
#c=cur.fetchone()
#print(c)


data=cur.fetchall()
for i in data:
    print(i)

#nm=input('Enter name searching: ')
nm=input('Enter name u want to delete: ')

cur.execute('select * from sample1 where name=%s',nm)
dt_nm=cur.fetchone()
print(dt_nm)

#pl=input('Enter updated location: ')
#cur.execute('update sample1 set place=%s where name=%s',(pl,nm))
#x.commit()

#cur.execute('select * from sample1 where name=%s',nm)
#dt_nm=cur.fetchone()
#print(dt_nm)

cur.execute('delete from sample1 where name=%s',nm)
x.commit()
cur.execute('select * from sample1')
nw_dt=cur.fetchall()
for j in nw_dt:
    print(i)
x.commit()

x.close()
