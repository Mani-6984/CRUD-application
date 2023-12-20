import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="likeit.")
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE Mydatabase")
mycursor.execute("CREATE TABLE TEACHER( Name VARCHAR(25), Age INT, DOB DATE, Number_of_Classes INT)")
