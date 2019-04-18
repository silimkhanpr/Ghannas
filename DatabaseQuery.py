import mysql.connector
from test import split
    #Db object
mydb = mysql.connector.connect(
        host="192.168.1.36",  #central db
        user="root@laptop",
        passwd="root",
        database="be_project"
    )
cursor=mydb.cursor()
def db_point(a,b):
  e=0
  uname1=""
  if b==1:
     query = "select Emp_id,Full_name from employee where ip_address=" + a   #query to get employee name based on ip address
     cursor.execute(query)
     result = cursor.fetchall()
     if (result):
       for x in result:
         uname1 = x[1]
         e = x[0]
  uname1=split(uname1,1)
  return uname1,e

def db_insert(val):
     sql = "insert into message (message_body,sender_id,receiver_group_id,message_type,time) values (%s,%s,%s,%s,%s)"   #query to insert a personal message into db
     cursor.execute(sql, val)
     mydb.commit()