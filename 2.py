import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user = "root",password = "rootroot",database="testdb")
my_cursor = mydb.cursor()

my_cursor.execute("%%TABLE employees")
#my_cursor.execute("CREATE TABLE empl(First_Name VARCHAR(255),Last_Name VARCHAR(255),Day INT(10),Gender VARCHAR(255),Salary INT(10),EMP_id INT(10),SUP_id INT(10))")
# stuff ="INSERT INTO employees(First_Name ,Last_Name ,Day ,Gender,Salary ,EMP_id,SUP_id ) VALUES (%s,%s,%s,%s,%s,%s,%s )"
# record = ("Markis","Steevexq<",13.54, "M","15000",5,1)
# my_cursor.execute(stuff, record)
#First_Name ,Last_Name ,Birth_day ,Gender,Salary ,Emp_id ,Supper_id e1,e2,e3, e4,e5,e6,e7  "Mark","Steeve","13/02", "M","15000","5","1"
mydb.commit()
