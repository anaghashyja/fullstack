import pymysql
print('-----------HELLO-----------')
x=pymysql.connect(host='localhost',username='root',password='asdlab',db='fruit')
cr=x.cursor()
cr.execute('create table department(name char(30),age int)')

x.close()
