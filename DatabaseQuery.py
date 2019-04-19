import mysql.connector
from test import split,server_config,encrypt_code
    #Db object
mydb = mysql.connector.connect(
        host=server_config(1),  #central db
        user="root@laptop",
        passwd="root",
        database="be_project"
    )
cursor=mydb.cursor()


def db_point(a, b):
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


def db_insert(val, a):

     if a == 1:  # query to insert a group message into db
        sql = "insert into message (message_body,sender_id,receiver_group_id,message_type,time) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, val)
        mydb.commit()
     elif a == 2:  # query to add new employee into db
         query = "INSERT INTO employee(Full_name, Designation, Email_id, Dob,ip_address) VALUES(%s, %s, %s, %s, %s)"
         cursor.execute(query, val)
         mydb.commit()
         eid=cursor.lastrowid
         uname = split(val[0])
         pass1 = encrypt_code("password")
         print(uname+"\t"+pass1)
         query = "INSERT INTO `users`(`Emp_id`, `username`, `password`, `user_type`)  VALUES(%s, %s ,%s, %s) "
         eval=(eid,uname,pass1,"standard")
         cursor.execute(query,eval)
         mydb.commit()


def group_message_populate():   #function to populate group messages from db
    sql= "SELECT sender_name,message_body FROM group_chat where group_id=3 ORDER BY `time` ASC "
    cursor.execute(sql)
    a=[]
    i=0
    result = cursor.fetchall()
    for x in result:
       a.append(x[0]+':'+x[1])
       i+=1
    return a,i


def user_login(uname):   #function to fetch user detail from db
    sql = "select * from users where username='"+uname+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# query for notices
def notice(search):
    if search!="null":            #Search a notice based on keyword
        query1 = "SELECT notice_body,date_created FROM `notices` WHERE (`notice_body` LIKE '%" + search + "%') ORDER BY " \
                                                                                             "`date_created` ASC "
    else:              #select all notices from db
        query1 = "SELECT notice_body,date_created FROM `notices`ORDER BY `date_created` ASC "
    cursor.execute(query1)
    result = cursor.fetchall()
    return result


# query to change password
def password_reset(p, t):
     sql = "UPDATE users SET password ='" + p + "'" + "WHERE Emp_iD ='" + t + "'"
     cursor.execute(sql)
     mydb.commit()

# query to get password of specific user from db
def get_password(t):
    sql = "select password from users where Emp_id='" + t + "'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        pass1 = x[0]
    return pass1


