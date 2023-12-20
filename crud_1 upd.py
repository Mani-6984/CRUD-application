import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="likeit.",database="Mydatabase")
mycursor=mydb.cursor()
t="TEACHER"
while(True):
    print("\n\n1.Show all teachers\n2.Add a Teacher\n3.Filter teachers based on criteria\n4.Search for a teacher\n5.Update a Teacher's record\n6.Delete a Teacher\n7.Get average number of classes\n8.Exit\n\n")
    n=int(input("Enter your choice: "))
    if n==1:
        mycursor.execute(f"SELECT * FROM {t}")
        for i in mycursor:
            print(i)
    elif n==2:
        try:
            nm=input("Enter Teacher's name: ")
            ag=int(input("Enter Teacher's age: "))
            dob=input("Enter Teacher's Date of Birth: ")
            nc=int(input("Enter the number of classes handled by the Teacher: "))
            mycursor.execute(f"INSERT INTO {t}(Name,Age,DOB,Number_of_Classes) VALUES('{nm}',{ag},'{dob}',{nc})")
        except Exception as e:
            print(str(e))
    elif n==3:
        try: 
            print("1.Filter by age\n2.Filter by the number of classes")
            ch=int(input("Enter your choice: "))
            if ch==1:
                print("Enter the age limit range: ")
                mn,mx=map(int,input().split())
                mycursor.execute(f"SELECT * FROM {t} WHERE Age BETWEEN {mn} AND {mx}")
                for i in mycursor:
                    print(i)
            if ch==2:
                print("Enter the class range: ")
                mn,mx=map(int,input().split())
                mycursor.execute(f"SELECT * FROM {t} WHERE Number_of_Classes BETWEEN {mn} AND {mx}")
                for i in mycursor:
                    print(i)
        except Exception as e:
                print(str(e))
        
    elif n==4:
        try:
            name=input("Enter the Teacher's Name: ")
            mycursor.execute(f"SELECT * FROM {t} WHERE Name='{name}'")
            for i in mycursor:
                print(i)
        except Exception as e:
                print(str(e))
    elif n==5:
        try:
            print("1.Update the entire record\n2.Update specific record")
            ch=int(input("Enter your choice: "))
            if ch==1:
                nm=input("Enter the name of the Teacher whose record needs to be updated: ")
                nmn=input("Enter the new name of the Teacher: ")
                ag=int(input("Enter the new age of the Teacher: "))
                dob=input("Enter the new DOB of the Teacher: ")
                nc=int(input("Enter the new number of classes handled by the Teacher: "))
                mycursor.execute(f"UPDATE {t} SET(Name='{nmn}',Age={ag},DOB='{dob}',Number_of_Classes={nc}) WHERE Name='{nm}' ")
            if ch==2:
                nm=input("Enter the name of the Teacher whose record needs to be updated: ")
                re=input("Enter the record that needs to be updated: ")
                l=['Name','DOB']
                if re not in l:
                    nv=int(input("Enter the updated record: "))
                    mycursor.execute(f"UPDATE {t} SET {re}={nv} WHERE Name='{nm}'")
                else:
                    nv=input("Enter the updated record: ")
                    mycursor.execute(f"UPDATE {t} SET {re}='{nv}' WHERE Name='{nm}'")
        except Exception as e:
                print(str(e))
    elif n==6:
        try:
            nm=input("Enter the name of the Teacher whose record is to be deleted: ")
            mycursor.execute(f"DELETE FROM {t} WHERE Name='{nm}'")
        except Exception as e:
                print(str(e))
    elif n==7:
        mycursor.execute(f"SELECT AVG(Number_of_Classes) FROM {t}")
        for i in mycursor:
            print(i)
    elif n==8:
        mydb.commit()
        break
    else:
        print("Enter a valid choice")
    mydb.commit()
