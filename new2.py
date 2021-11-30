import pymysql
x=pymysql.connect(host='localhost',user='root',password='asdlab',db='avodha')
cur=x.cursor()

print('haiiiiiiiiii')
a=input('Enter name of the customer plz:')
b=input('Enter age of the customer:')
c=input('Enter location to track:')

cur.execute("insert into customer values(%s,%s,%s)",(a,b,c))

x.commit()
chk="select * from customer where name=%s"
cur.execute(chk,a)
cr=cur.fetchall()
print('Details of the user is: \n')
for i in cr:
    print(i)

x.close()
