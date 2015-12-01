import mysql.connector
conn = mysql.connector.connect(user="root", password = "arsenal", host = "localhost", database = 'allproject')
mycursor = conn.cursor()
Users=[]
namesql = input("Write a workers name")
mycursor.execute("SELECT * FROM users WHERE name=%s", (namesql,))
print(mycursor.fetchall())


##Users=[]
###namesql = input("Write a workers name")
##mycursor.execute("SELECT * FROM users")
##mylist=mycursor.fetchall()
##for x in mylist:
##    Users.append(x)
##print(Users[0][1])

##mylist=mycursor.fetchall()
##for x in mylist:
##    Users.append(x)
##print(Users[0][1])
