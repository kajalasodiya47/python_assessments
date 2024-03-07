# import modules
from tkinter import *
import pymysql
import random
# import call through subprocess module
from subprocess import call

# opens a file for append a text
f = open("recepit.txt","a")
f.seek(0)
# for empty content
f.truncate()

# create a function for add guest details in database
def database(value):
    name = value['name']
    address = value['address']
    number = value['number']
    days = value['days']
    var1 = value['var1']
    var2 = value['var2']
    var3 = value['var3']
    var4 = value['var4']
    var5 = value['var5']
    var6 = value['var6']
    # ladder else-if
    if var1 == 1:
      room_list = [26,23,12]
      # get the randomly listitem
      room_no = random.choice(room_list)
      room = str(room_no)
      price = str(1000)
    elif var2 == 1:
      room_list = [24,22,9]
      # get the randomly listitem
      room_no = random.choice(room_list)
      room = str(room_no)
      price = str(2000)
    elif var3 == 1:
      room_list = [20,19,2]
      # get the randomly listitem
      room_no = random.choice(room_list)
      room = str(room_no)
      price = str(500)
    elif var4 == 1:
      room_list = [3,13,28]
      # get the randomly listitem
      room_no = random.choice(room_list)
      room = str(room_no)
      price = str(1800)
      
    # database connection  
    mydb = pymysql.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()

    # create database
    mycursor.execute("create database if not exists hotelmanagementdb")
    mydb.commit()

    mydb = pymysql.connect(host="localhost",user="root",password="",database="hotelmanagementdb")
    mycursor = mydb.cursor()

    # create table
    mycursor.execute("create table if not exists guest_details(id int primary key auto_increment,name varchar(20),address varchar(30),mobile varchar(10),room_type varchar(20),payment_method varchar(40))")
    mydb.commit()

    # insert guest details into table
    mycursor.execute("insert into guest_details(name,address,mobile,no_of_days,delux_room,full_delux_room,general_room,joint_room,payment_by_cash,payment_by_credit_debit,room_no,price) values ('" + name + "','" + address + "','" + number + "','" + days + "','" + str(var1) + "','" + str(var2) + "','" + str(var3) + "','" + str(var4) + "','" + str(var5) + "','" + str(var6) + "','" + room + "','" + str(price) + "')")
    mydb.commit()
    
    # writes a contents into file 
    f.write("\nName : "+name)
    f.write("\nAddress : "+address)
    f.write("\nNumber : "+number)
    f.write("\nRoom No : "+room)
    f.write("\nBill : "+price)
    f.close() 

# create a function for add user data in database       
def database1(value):
    name = value['name']
    contact = value['contact']
    email = value['email']
    gender = value['gender']
    city = value['city']
    state = value['state']
    # database connection
    mydb = pymysql.connect(host="localhost",user="root",password="",database="hotelmanagementdb")
    mycursor = mydb.cursor()
    # create database
    mycursor.execute("create table if not exists user_details(id int primary key auto_increment,name varchar(20),contact varchar(10),email varchar(20),gender int,city varchar(15),state varchar(15))")
    mydb.commit()
    # insert user details
    mycursor.execute("insert into user_details(name,contact,email,gender,city,state) values ('" + name + "','" + contact + "','" + email + "','" + gender + "','" + city + "','" + state + "')")
    mydb.commit()
    call(["python", "checkin.py"])
 
