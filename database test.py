import mysql.connector
conn=mysql.connector.connect(user='root',password='arsenal', host= 'localhost')
mycursor=conn.cursor()
mycursor.execute("CREATE DATABASE allproject")
mycursor.execute("USE allproject")
mycursor.execute("""CREATE TABLE users (
                     `ID` int(5) NOT NULL ,
		     `name` char(50) NOT NULL,
		     `Device` VARCHAR(50) NOT NULL,
                     `timestamp` TIME NOT NULL,
                     `coordinate x` FLOAT NOT NULL,
                     `coordinate y` FLOAT NOT NULL,
                     `coordinate z` FLOAT NOT NULL,
                     `Accuracy` int NOT NULL,
                     `Datasource` char(3) NOT NULL,
                     `Datatype` int(5) NOT NULL)""")
                      
