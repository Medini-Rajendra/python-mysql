import mysql.connector

class DBHelper:
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',
                port='3306',
                user='root',
                password='root',
                database='pythontest',
                auth_plugin='mysql_native_password')
        query='create table if not exists user(userId int primary key, username varchar(40), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    def insertdb(self,userid, username, phone):
        query="insert into user(userId, username, phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
    def fetchall(self):
        query="select * from user";
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur: 
            print(row)
    def deleteuser(self,userId):
        query="delete from user where userId={}".format(userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("deleted")

#main coding
#helper=DBHelper()
#helper.insertdb(3534,'krishna',"4343443")
#helper.insertdb(6454,'mukunda',"4343443")
#helper.insertdb(4534,'hari',"4343443")
#helper.insertdb(345,'gopal',"4343443")
#helper.deleteuser(4534)
#helper.fetchall()

