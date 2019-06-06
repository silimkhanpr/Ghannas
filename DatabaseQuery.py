import mysql.connector
from test import split, server_config, encrypt_code
# Db object
mydb = mysql.connector.connect(
        host=server_config(1),  # central db
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
    result = db_point(query)
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
         eval = (eid, uname, pass1, "standard")
         cursor.execute(query, eval)
         mydb.commit()
     elif a == 3:      # query to insert notices into db
         sql = "INSERT INTO notices(leader_id, notice_body, date_created) VALUES(%s, %s, %s)"
         cursor.execute(sql, val)
         mydb.commit()


# function to populate messages from db
def message_populate(j, b="null"):
    if j != "null" and b != "null":            # code to populate personal chat from db
        global query1
        query1 = "SELECT `sender_name`, `message_body` FROM `personal_chat` where (" \
                       "`sender_id`='" + str(j) + "' and `receiver_id`='" + str(b) + "') OR (`sender_id`='" + str(b) \
                       + "' and `receiver_id`='" + str(j) + "') ORDER BY `time` DESC "
    else:              # select all notices from db

        query1 = "SELECT sender_name,message_body FROM group_chat where group_id='"+str(j)+"' ORDER BY `time` DESC "
    a = []
    i = 0
    print(j+":"+b)
    result = db_point(query1)
    for x in result:
        a.append(x[0] + ':' + x[1])
        i += 1
    return a, i


# query to change password
def password_reset(p, t):
    sql = "UPDATE users SET password ='" + p + "'" + "WHERE Emp_iD ='" + str(t) + "'"
    cursor.execute(sql)
    mydb.commit()


# query to get password of specific user from db
def get_password(t):
    sql = "select password from users where Emp_id='" + str(t) + "'"
    result = db_point(sql)
    for x in result:
        pass1 = x[0]
    return pass1


# query to update ip address of user
def update_ip(e, t):
    sql = "UPDATE employee SET ip_address ='" + t + "'" + "WHERE Emp_iD ='" + str(e) + "'"
    cursor.execute(sql)
    mydb.commit()


