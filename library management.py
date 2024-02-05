import mysql.connector
mydb=mysql.connector.connect (host="localhost", user="root", password="admin")
from tkinter import *


mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")
while True:
    print('''1.admin
             2.user''')
    xx=int(input("ADMIN/LOGIN(1,2)):"))
    if xx==1:
        
#ADMIN

        while True:
            print("""1:Signup
                     2:Login"""
                  )

            ch=int(input("SIGNUP/LOGIN(1,2):"))


            if ch==1:

                username=input("USERNAME:")
                pw=input("PASSWORD:")

                mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
                mydb.commit()


            elif ch==2:

                username=input("USERNAME:")

                mycursor.execute("select username from signup where username='"+username+"'")
                checku=mycursor.fetchone()

                if check is not None:
                    print("VALID USERNAME!!")

                    pw=input("PASSWORD:")

                    mycursor.execute("select password from signup where password='"+pw+"'")
                    checkp=mycursor.fetchone()

                    if checkp is not None:
                        print("""**********************************
                 LOGIN SUCCESSFULL
        **********************************""")

                        print("""======================================================================
                                       MY BOOK STORE    
        =======================================================================""")

                        mycursor.execute("create table if not exists Available_Books(BookId int(5),BookName varchar(30) primary key,Genre varchar(20),Quantity int(3),Author varchar(20),Publication varchar(30),Price int(4))")
                        mycursor.execute("create table if not exists Sell_rec(bookID int(5),CustomerName varchar(20),PhoneNumber char(10) unique key, BookName varchar(30),Quantity int(100),Price int(4),foreign key (BookName) references Available_Books(BookName))")
                    
                        mydb.commit()

                    while(True):
                            print("""1:Add Books
                                     2:Available Books
                                     3:Search Books
                                     4:Sell Record
                                     5:Available Books 
                                     6:Exit""")

                            a=int(input("Enter your choice:"))

          
                            if a==1:

                                print("All information  are mandatory to be filled")
                
                                bookid=int(input("enter book id"))
                                book=str(input("Enter Book Name:"))
                                genre=str(input("Genre:"))
                                quantity=int(input("Enter quantity:"))        
                                author=str(input("Enter author name:"))
                                publication=str(input("Enter publication house:"))
                                price=int(input("Enter the price:"))

                                mycursor.execute("select * from Available_Books where bookname='"+book+"'")
                                row=mycursor.fetchone()

                                if row is not None:
                                    mycursor.execute("update Available_Books set quantity=quantity+'"+str(quantity)+"' where bookname='"+book+"'")
                                    mydb.commit()

                                    print("""************************
         SUCCESSFULLY ADDED
        *********************""")
                                
                                
                                else:
                                    mycursor.execute("insert into Available_Books(bookname,genre,quantity,author,publication,price) values('"+book+"','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"')")
                                    mydb.commit()

                                    print("""++++++++++++++++++++++
        ++SUCCESSFULLY ADDED++
        ++++++++++++++++++++++""") 
                           

            
                            elif a==2:                

                                print("AVAILABLE BOOKS...")

                                mycursor.execute("select * from Available_Books ")
                                for x in mycursor:
                                    print(x)
                              
                                cusname=str(input("Enter customer name:"))
                                phno=int(input("Enter phone number:"))
                                book=str(input("Enter Book Name:"))
                                price=int(input("Enter the price:"))
                                n=int(input("Enter quantity:"))

                                mycursor.execute("select quantity from available_books where bookname='"+book+"'")
                                lk=mycursor.fetchone()

                                if max(lk)<n:
                                    print(n,"Books are not available!!!!")

                                else:
                                    mycursor.execute("select bookname from available_books where bookname='"+book+"'")
                                    ld=mycursor.fetchone()

                                    if ld is not None:
                                        mycursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+book+"','"+str(n)+"','"+str(price)+"')")
                                        mycursor.execute("update Available_Books set quantity=quantity-'"+str(n)+"' where BookName='"+book+"'")
                                        mydb.commit()

                                        print("""************************
         BOOK HAS BEEN SOLD
        ************************""")

                                    else:
                                        print("BOOK IS NOT AVAILABLE!!!!!!!")

           
                            elif a==3:

                                print("""1:Search by name
                                         2:Search by genre
                                         3:Search by author""")

                                l=int(input("Search by?:"))

                
                                if l==1:
                                    o=input("Enter Book to search:")

                                    mycursor.execute("select bookname from available_books where bookname='"+o+"'")
                                    tree=mycursor.fetchone()

                                    if tree!=None:
                                        print("""************************
           BOOK IS IN STOCK
        ************************""")

                                    else:
                                        print("BOOK IS NOT IN STOCK!!!!")

                
                                elif l==2:
                                    g=input("Enter genre to search:")

                                    mycursor.execute("select genre from available_books where genre='"+g+"'")
                                    poll=mycursor.fetchall()

                                    if poll is not None:
                                        print("""************************
          BOOK IS IN STOCK
        ************************""")

                                        mycursor.execute("select * from available_books where genre='"+g+"'")

                                        for y in mycursor:
                                            print(y)

                                    else:
                                        print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!")


               
                                elif l==3:
                                    au=input("Enter author to search:")

                                    mycursor.execute("select author from available_books where author='"+au+"'")
                                    home=mycursor.fetchall()

                                    if home is not None:
                                        print("""************************
          BOOK IS IN STOCK
        ************************""")

                                        mycursor.execute("select * from available_books where author='"+au+"'")

                                        for z in mycursor:
                                            print(z)

                                    else:
                                        print("BOOKS OF THIS AUTHOR ARE NOT AVAILABLE!!!!!!!")
                                mydb.commit()

           

                                        
                            elif a==4:
                                print("1:Sell history details")
                                print("2:Reset Sell history")

                                ty=int(input("Enter your choice:"))

                                if ty==1:
                                    mycursor.execute("select * from sell_rec")
                                    for u in mycursor:
                                        print(u)

                                if ty==2:
                                    bb=input("Are you sure(Y/N):")

                                    if bb=="Y":
                                        mycursor.execute("delete from sell_rec")
                                        mydb.commit()

                                    elif bb=="N":
                                        pass

            
                            elif a==5:
                                mycursor.execute("select * from available_books order by bookname")
                                for v in mycursor:
                                    print(v)

            
                               
                            elif a==6:
                                break


                    else:
                        print("""++++++++++++++++++++++
        ++INCORRECT PASSWORD++
        ++++++++++++++++++++++""")


                else:
                    print("""++++++++++++++++++++
        ++INVALID USERNAME++
        ++++++++++++++++++++""")

            else:
                    break
#USER
   
    if xx==2:
        print('''****************************
       WELCOME
*****************************''')
        
        cursor.execute("SELECT * FROM Available_Books")
        dis=cursor.fetchall()
        for i in dis:
            print(dis)
        

        def myclick():
            print("Please fill in the details")
            bkid=int(input("enter book id"))
            nameb=input("enter your name")
            phoneno=int(input("enter your phone number"))
            bkname=int(input("enter the name of the book"))
            quant=int(input("enter quantity of book"))
            pricee=int(input("enter price"))
            cursor.execute("SELECT Quantity FROM Available_Books WHERE BookName='"+nameb+"' ")
            chk=cursor.fetchall()
            for i in chk:
                if chk==0:
                    print("NO STOCK LEFT!!!!")
                else:
                    break
            cursor.execute("insert into Sell_rec values('"+bkid+"','"+nameb+"','"+phoneno+"','"+bkname+"','"+quant+"','"+pricee+"'")
            print('''***********************
         ORDER SUCCESFULL
***********************''')
            
        btn=Button(tk,text="click to buy books ",command =myclick)
        btn.pack()
        
       

                
        
        

        

    
