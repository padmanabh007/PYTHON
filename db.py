import sqlite3 as lt #for database 

#functionality goes here
class databaseManage(object):#Creating a database 
    def __init__(self):
        global con
        try:
            con=lt.connect('courses.db')
            with con:
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Description TEXT,Price TEXT,is_Private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB")

    #Insert data in data base
    def insert_Data(self,data):
        try:
            with con:
                cur=con.cursor()
                cur.execute("INSERT INTO course(Name,Description,Price,is_Private) VALUES(?,?,?,?)",data)
                return True
        except Exception:
            return False

    #Fetch data in data base
    def fetch_Data(self):
        try:
            with con:
                cur=con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

   #Delete data in data base
    def delete_Data(self,id):
        try:
            with con:
                cur=con.cursor()
                sql="DELETE FROM course WHERE id=?"
                cur.execute(sql ,[id])
                return True
        except Exception:
            return False

#Interface to the user
def main():
    print("*"*40)
    print("\nCourse management::\n")
    db=databaseManage()
    print("User Manual\n")
    print("Enter your choice\n")
    print('1.Insert a course\n2.Show all course details\n3.Delete a course using course id\n')
    ch=input("Enter ")

#For inserting data into the database by the users choice
    if ch=="1":
        name    = input("\nCourse  name ")
        descp   = input("Descpition ")
        price   = input("Amount ")
        private = input("Is the couse private or not(0/1) ")

        #Multiple info
        if db.insert_Data([name,descp,price,private]):
            print("Course inserted  successfully")
        else:
            print("OOPS something Wrong!")

 #For listing the data stored in the data base  by the users choice       
    elif ch=="2":
        print("\nCourse list")
        for iteam in db.fetch_Data():
            print("Course ID:"+str(iteam[0]))
            print("Course ID:"+str(iteam[1]))
            print("Description:"+str(iteam[2]))
            print("Price:"+str(iteam[3]))
            private= 'Yes' if iteam[4] else 'NO'
            print("IS_PRIVATE:"+private)
            print("\n")

#For deleting th data from the database 
    elif ch=="3":
        record_id=input("Enter course ID")
        if db.delete_Data(record_id):
            print("Deleted sucesssfully")
        else:
            print("oops")

#If the users choice is wrong   
    else:
        print("Wrong input")

if __name__=='__main__': #For executing the main function
    main()

            