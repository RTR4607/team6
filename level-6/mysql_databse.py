import mysql.connector
class Mysql_DBaccess:
    def __init__(self,host,db,user,password):
        self.host=host
        self.db = db
        self.user=user
        self.password=password
        try:
            self.connection=mysql.connector.connect(host=self.host,database=self.db,user=self.user,password=self.password)
        except:
            print("Error while  into connecting to the database")
    def inser_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql="insert into files(filename) values(%s);"
        val=(self.filename)
        self.cur.execute(sql,(val,))
        self.connection.commit()

    def search(self):
        self.cur=self.connection.cursor()
        sql="select * from files limit 0,10;"
        self.cur.execute(sql)
        self.connection.commit()
    def search_db(self,fil):
        self.cur = self.connection.cursor()
        sql="select * from files where filename like '%{0}'".format(fil)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row==0:
            return 0
        else:
            return row
        '''if row==obj.find_file():
            print(row)
        else:
            print(obj.find_file(self.filename,self.filepath))'''



obj=Mysql_DBaccess('localhost','student_db','root','root')
#obj.inser_data('C:/Users\\user787\\PycharmProjects\\one1.txt')
print(obj.search_db('one.txt'))