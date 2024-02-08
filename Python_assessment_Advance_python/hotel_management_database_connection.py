# import modules
import tkinter
from tkinter import *
import pymysql
import random
# opens a file for append a text
f = open("recepit.txt","a")
f.seek(0)
# for empty content
f.truncate()

# create a Database named class
class Database:
  # private access specifier  
  __price = None
  
  # member method
  def database(self,value):
    self.__name = value['name']
    self.__address = value['address']
    self.__number = value['number']
    self.days = value['days']
    self.var1 = value['var1']
    self.var2 = value['var2']
    self.var3 = value['var3']
    self.var4 = value['var4']
    self.var5 = value['var5']
    self.var6 = value['var6']
    # ladder else-if
    if self.var1 == 1:
      room_list = [26,23,12]
      # get the randomly listitem
      room_no = random.choice(room_list)
      self.room = str(room_no)
      self.__price = str(1000)
      
    elif self.var2 == 1:
      room_list = [24,22,9]
      # get the randomly listitem
      room_no = random.choice(room_list)
      self.room = str(room_no)
      self.__price = str(2000)
      
    elif self.var3 == 1:
      room_list = [20,19,2]
      # get the randomly listitem
      room_no = random.choice(room_list)
      self.room = str(room_no)
      self.__price = str(500)
      
    elif self.var4 == 1:
      room_list = [3,13,28]
      # get the randomly listitem
      room_no = random.choice(room_list)
      self.room = str(room_no)
      self.__price = str(1800)
      
    # database connection  
    mydb = pymysql.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    # create database
    mycursor.execute("create database if not exists hotel_management_db")
    mydb.commit()

    mydb = pymysql.connect(host="localhost",user="root",password="",database="hotel_management_db")
    mycursor = mydb.cursor()
    # create table
    mycursor.execute("create table if not exists guest_details(id int primary key auto_increment,name varchar(20),address varchar(30),mobile varchar(10),room_type varchar(20),payment_method varchar(40))")
    mydb.commit()
    # insert guest details into table
    mycursor.execute("insert into guest_details(name,address,mobile,no_of_days,delux_room,full_delux_room,general_room,joint_room,payment_by_cash,payment_by_credit_debit,room_no,price) values ('" + self.__name + "','" + self.__address + "','" + self.__number + "','" + self.days + "','" + str(self.var1) + "','" + str(self.var2) + "','" + str(self.var3) + "','" + str(self.var4) + "','" + str(self.var5) + "','" + str(self.var6) + "','" + self.room + "','" + str(self.__price) + "')")
    mydb.commit()
    
  # another member method
  def __Display(self):
     # writes a contents into file 
     f.write("\nName : "+self.__name)
     f.write("\nAddress : "+self.__address)
     f.write("\nNumber : "+self.__number)
     f.write("\nRoom No : "+self.room)
     f.write("\nBill : "+(self.__price))
     
  # create a member method for show private members
  def access(self):
       self.__Display()
       
  # create another member method
  def database1(self,value):
    self.name = value['name']
    self.contact = value['contact']
    self.email = value['email']
    self.gender = value['gender']
    self.city = value['city']
    self.state = value['state']
    # database connection
    mydb = pymysql.connect(host="localhost",user="root",password="",database="hotel_management_db")
    mycursor = mydb.cursor()
    # create database
    mycursor.execute("create table if not exists user_details(id int primary key auto_increment,name varchar(20),contact varchar(10),email varchar(20),gender int,city varchar(15),state varchar(15))")
    mydb.commit()
    # insert user details
    mycursor.execute("insert into user_details(name,contact,email,gender,city,state) values ('" + self.name + "','" + self.contact + "','" + self.email + "','" + self.gender + "','" + self.city + "','" + self.state + "')")
    mydb.commit()

  # member method for show gusest 
  def show_guest(self):
    # database connection
    mydb = pymysql.connect(host="localhost",user="root",password="",database="hotel_management_db")
    mycursor = mydb.cursor()
    # use select query to get name, room no
    mycursor.execute("select name , room_no from guest_details")
    data = mycursor.fetchall()
    return data
  
  # member method for check the room details
  def check_room(self,room_no):
    self.room_no = room_no
    # database connection
    mydb = pymysql.connect(host="localhost",user="root",password="",database="hotel_management_db")
    mycursor = mydb.cursor()
    # use select query to get name
    mycursor.execute("select name from guest_details where room_no = '" + str(self.room_no) + "'")
    data = mycursor.fetchone()
    return data
  
  # member method for to get guest details
  def get_guest_details(self,room_no):
    self.room_no = room_no
    # database connection 
    mydb = pymysql.connect(host="localhost",user="root",password="",database="hotel_management_db")
    mycursor = mydb.cursor()
    # use select query to get all guest details
    mycursor.execute("select name,address,mobile from guest_details where room_no = '" + str(self.room_no) + "'")
    data = mycursor.fetchone()
    return data
    

