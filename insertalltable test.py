import mysql.connector
conn = mysql.connector.connect(user="root", password = "arsenal", host = "localhost", database = 'allproject')
mycursor = conn.cursor()

mycursor.execute("""INSERT INTO users VALUES
(1,\
"Daniel",\
"46fee5217f7a58cb ",\
"45870139502041 ",\
"1.2720693 ",\
"6.583606 ",\
"6.8299093 ",\
" 3 ",\
"Acc ",\
"1")""")

mycursor.execute("""INSERT INTO users VALUES
(2,\
"Briyanka",\
"46fee5217f7a58cb ",\
"45873179636163 ",\
"1.2313678 ",\
" 6.696133  ",\
"6.8299093 ",\
" 3 ",\
"Acc ",\
"1")""")
