import mysql.connector
conn = mysql.connector.connect(user="root", password = "arsenal", host = "localhost", database = 'allproject')
mycursor = conn.cursor()
Users=[]
namesql = int(input("write a number corresponding to the worker in the documentation to see their activity"))
mycursor.execute("SELECT * FROM users")
mylist=mycursor.fetchall()
for x in mylist:
    Users.append(x)
name = Users[(namesql)][1]
time = Users[(namesql)][3]
x = Users[(namesql)][4]
y = Users[(namesql)][5] 
z = Users[(namesql)][6]
if x > 0.4628291 and y > 7.0528693 and z > 6.9280715:
    print( name, " was sitting down and working at this time", time)
else:
    print(name, " was walking at this time ", time )

