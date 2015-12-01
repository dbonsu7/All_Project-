import mysql.connector


class Database:
    def __init__(self, database, Tablename,):
        self.db = allproject
        self.Tablename = users

        self.cnx = mysql.connector.connect(user = 'root',
                                    password = 'd4n14l',
                                    host = 'localhost')
        


#Cursor allows us to send commands to the database to execute commands
        self.cursor = self.cnx.cursor()

    def ConnectToDatabase(self):
        try:
            self.cnx.database = self.db #attempts to create the database by setting its name
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.CreateDatabase()
                self.cnx.database = self.db#if no database exists using that name it will create one
            else:
                print(err.msg)

    def CreateDatabase(self):
        try:
            mycursor.execute("CREATE DATABASE allproject")

    def CreateTable(self):#if table does not exists create tables with these colunms
        cmd = (" CREATE TABLE IF NOT EXISTS " + self.Tablename + " ("
            "`ID` int(5) NOT NULL AUTO_INCREMENT,"
                         "`name` char(50) NOT NULL,"
                         "  `Device` VARCHAR(50) NOT NULL,"
                        " `timestamp` int(50) NOT NULL,"#The sensor timestamp is actually nanoseconds of uptime needs to be converted
                         "`coordinate x` FLOAT NOT NULL,"
                         "`coordinate y` FLOAT NOT NULL,"
                        " `coordinate z` FLOAT NOT NULL,"
                        " `Accuracy` FLOAT NOT NULL,"
                        " `Datasource` char(5) NOT NULL,"
                        " `Datatype` int(5) NOT NULL,"
                        " PRIMARY KEY (`ID`))"
            ") ENGINE=InnoDB;")
        self.RunCommand(cmd)


            
    




    def RunCommand(self, cmd):#in case of any errors

        print ("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print ('ERROR MESSAGE: ' + str(err.msg))
            print ('WITH ' + cmd)
        try:
            msg = self.cursor.fetchall()#trying to get all output data from MYSQL
        except:
            msg = self.cursor.fetchone()
        return msg



    def __del__(self):#Deconstructer class
        self.cnx.commit()#This commits the changes to the database
        self.cursor.close()
        self.cnx.close()#closes the connection



if __name__ == '__main__':
    db = 'allproject'
    Tablename = 'users'
    


    dbu = DatabaseUtility(db, Tablename)

                 
                 

 




