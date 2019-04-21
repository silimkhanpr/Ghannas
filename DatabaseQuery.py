import mysql.connector
from test import split, server_config, encrypt_code
# Db object
mydb = mysql.connector.connect(
        host=server_config(1),  #central db
        user="root@laptop",
        passwd="root",
        database="be_project"
    )
cursor = mydb.cursor()


def db_point(a):
    cursor.execute(a)
    result = cursor.fetchall()
    return result


def emp_ip(a):
    e = 0
    u = ""
    # query to get employee name based on ip address
    query = "select Emp_id,Full_name from employee where ip_address=" + a
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
      for x in result:
       u = x[1]
       e = x[0]
    u = split(u, 1)
    return u, e


# function to insert values in db
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
         uname = split(val[0])   # function call to get username
         pass1 = encrypt_code("password")    # function call to encrypt password
         print(uname+"\t"+pass1)
         # create user in user table
         query = "INSERT INTO `users`(`Emp_id`, `username`, `password`, `user_type`)  VALUES(%s, %s ,%s, %s) "
         eval = (eid,uname,pass1,"standard")
         cursor.execute(query,eval)
         mydb.commit()


# function to populate messages from db
def message_populate(a, b):
    if a != "null" and b != "null":            # code to populate personal chat from db
        global query1
        query1 = "SELECT `sender_name`, `message_body`, `time` FROM `personal_chat` where (" \
                       "`sender_id`='" + str(a) + "' and `receiver_id`='" + str(b) + "') OR (`sender_id`='" + str(b) \
                       + "' and `receiver_id`='" + str(a) + "') ORDER BY `time` ASC "
    else:              # select all notices from db

        query1 = "SELECT sender_name,message_body FROM group_chat where group_id=3 ORDER BY `time` ASC "
    a = []
    i = 0
    cursor.execute(query1)
    result = cursor.fetchall()
    for x in result:
        a.append(x[0] + ':' + x[1])
        i += 1
    return a, i


def user_login(u):   # function to fetch user detail from db
    sql = "select * from users where username='"+u+"'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# query for notices
def notice(search):
    if search != "null":            # Search a notice based on keyword
        global query1
        query1 = "SELECT notice_body,date_created FROM `notices` WHERE (`notice_body` LIKE '%" + search + "%') ORDER " \
                 "BY `date_created` ASC "

    else:              # select all notices from db
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


