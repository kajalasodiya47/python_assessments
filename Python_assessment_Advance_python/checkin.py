# import modules
from tkinter import *
# import call through subprocess module
from subprocess import call
# import database connection file for perform database operations
import hotel_management_database_connection 

# call Tk class object
root = Tk()
# set title and geometry for window
root.title("HOTEL MANAGEMENT")
root.geometry('700x500')
root.configure(bg="white")

# create a function for name validation 
def chk_name():
    while True:
        # get the value of name field using get() method
        k = name.get()
        if len(k) != 0:
            Text1.insert(INSERT, "name has been inputed""\n")
            break
        else:
            Text1.insert(INSERT, "Please enter a name""\n")
            break
                
# create a function for address validation            
def chk_add():
    while True:
        # get the value of address field using get() method
        s = addr.get()
        if len(s) != 0:
            Text1.insert(INSERT, "address has been inputed""\n")
            break
        else:
            Text1.insert(INSERT, "Please enter a address""\n")
            break
                
# create a function for mobile validation            
def chk_mo():
    while True:
        # get the value of mobile field using get() method
        h = mobile.get()
        if len(h) != 0 and len(h) == 10:
            Text1.insert(INSERT, "mobile number has been inputed""\n")
            break
        else:
            Text1.insert(INSERT, "Please enter a mobile number""\n")
            break
                
# create a function for day validation           
def chk_day():
    while True:
        # get the value of days field using get() method 
        m = days.get()
        if len(m) != 0:
            Text1.insert(INSERT, "days has been inputed""\n")
            break
        else:
            Text1.insert(INSERT, "Please enter a days""\n")
            break
                
# create a function for add guest data in database
def submit_clicked():
        # use get() method to get values
        name = Entry1.get()
        address = Entry2.get()
        number = Entry3.get()
        days = Entry4.get()
        global var1
        var1 = var1.get()
        global var2
        var2 = var2.get()
        global var3
        var3 = var3.get()
        global var4
        var4 = var4.get()
        global var5
        var5 = var5.get()
        global var6
        var6 = var6.get()
        # dictionary for store values
        dict1 = {'name':name,'address':address,'number':number,'days':days,'var1':var1,'var2':var2,'var3':var3,'var4':var4,'var5':var5,'var6':var6}
        hotel_management_database_connection.database(dict1)
        Text1.insert(INSERT, "data added""\n")
        

# Frame widgets
Frame1 = Frame(root,relief=GROOVE,borderwidth="2",background="#ffffff")
Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)

# Message widgets
Message1 = Message(Frame1,text='''YOU CLICKED ON''', font=("Arial", 15,"bold"),background="#ffffff",width=496)
Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)

# Message widgets
Message2 = Message(Frame1,text=''':''', font=("Arial", 15,"bold"),background="#ffffff",width=66)
Message2.place(relx=0.52, rely=0.19, relheight=0.74, relwidth=0.07)

# Message widgets
Message3 = Message(Frame1,text='''CHECK INN''', font=("Arial", 15,"bold"),background="#ffffff",width=347)
Message3.place(relx=0.57, rely=0.11, relheight=0.79, relwidth=0.35)

# Frame widgets
Frame2 = Frame(root,relief=GROOVE,borderwidth="2",background="#ffffff")
Frame2.place(relx=0.03, rely=0.18, relheight=0.59, relwidth=0.93)

# Label widgets for guest name
Label1 = Label(Frame2,text='''ENTER YOUR NAME''',font=("Arial",9,"bold"),background="#ffffff")
Label1.place(relx=0.05, rely=0.03, height=47, width=289)

# message widgets
Message4 = Message(Frame2,text=''':''',font=("Arial",10,"bold"),background="#ffffff")
Message4.place(relx=0.41, rely=0.07, relheight=0.1, relwidth=0.05)

# entry widgets for guest name
Entry1 = Entry(Frame2,background="#ffffff")
name=StringVar()
Entry1.place(relx=0.47, rely=0.05,height=28, relwidth=0.33)
Entry1.configure(textvariable=name)

# button widgets for guest name
Button1 = Button(Frame2,text='''OK''',font=("Arial",10,"bold"),pady="0",background="#ffffff")
Button1.place(relx=0.91, rely=0.05, height=30, width=43)
Button1.configure(command=chk_name)

# label widgets for guest address
Label2 = Label(Frame2,text='''ENTER YOUR ADDRESS''',font=("Arial",9,"bold"),background="#ffffff")
Label2.place(relx=0.032, rely=0.15, height=47, width=334)

# message widgets
Message5 = Message(Frame2,text=''':''',font=("Arial",10,"bold"),background="#ffffff")
Message5.place(relx=0.42, rely=0.18, relheight=0.12, relwidth=0.03)

# Entry widgets for guest address
Entry2 = Entry(Frame2,background="#ffffff")
addr = StringVar()
Entry2.place(relx=0.47, rely=0.18,height=28, relwidth=0.33)
Entry2.configure(textvariable=addr)

# button widgets for guest address
Button2 = Button(Frame2,text='''OK''',font=("Arial",10,"bold"),pady="0")
Button2.place(relx=0.91, rely=0.18, height=30, width=43)
Button2.configure(command=chk_add)

# label widgets for guest mobile number
Label3 = Label(Frame2,text='''ENTER YOUR NUMBER''',font=("Arial",9,"bold"),background="#ffffff")
Label3.place(relx=0.032, rely=0.28, height=47, width=329)

# message widgets
Message6 = Message(Frame2,text=''':''',font=("Arial",10,"bold"),background="#ffffff")
Message6.place(relx=0.415, rely=0.3, relheight=0.09, relwidth=0.04)

# Entry widgets for guest mobile number
Entry3 = Entry(Frame2,background="#ffffff")
mobile=StringVar()
Entry3.place(relx=0.47, rely=0.30,height=28, relwidth=0.33)
Entry3.configure(textvariable=mobile)

# button widgets for guest mobile number
Button3 = Button(Frame2,text='''OK''',font=("Arial",10,"bold"),background="#ffffff",pady="0")
Button3.place(relx=0.91, rely=0.31, height=30, width=43)
Button3.configure(command=chk_mo)

# label widgets for guest number of days
Label4 = Label(Frame2,text='''NUMBER OF DAYS''',font=("Arial",9,"bold"),background="#ffffff")
Label4.place(relx=0.07, rely=0.40, height=44, width=260)

# message widgets  
Message7 = Message(Frame2,text=''':''',font=("Arial",10,"bold"),background="#ffffff")
Message7.place(relx=0.41, rely=0.42, relheight=0.11, relwidth=0.04)

# entry widgets for guest number of days
Entry4 = Entry(Frame2,background="#ffffff")
days=StringVar()
Entry4.place(relx=0.47, rely=0.43, height=28, relwidth=0.33)
Entry4.configure(textvariable=days)

# button widgets for guest number of days
Button4 = Button(Frame2,text='''OK''',font=("Arial",10,"bold"),background="#ffffff",pady="0")
Button4.place(relx=0.91, rely=0.43, height=30, width=43)
Button4.configure(command=chk_day)

# label widgets for guest room
Label5 = Label(Frame2,text='''CHOOSE YOUR ROOM''',font=("Arial",9,"bold"),background="#ffffff")
Label5.place(relx=0.32, rely=0.5, height=48, width=296)

# checkbutton widgets for guest deluxe room
Checkbutton1 = Checkbutton(Frame2,text='''DELUXE''',font=("Arial",9,"bold"),justify=LEFT,background="#ffffff")
var1 = IntVar()
var1.set(0)
Checkbutton1.place(relx=0.28, rely=0.58, relheight=0.17
                , relwidth=0.14)
Checkbutton1.configure(variable=var1)

# checkbutton widgets for guest full deluxe room
Checkbutton2 = Checkbutton(Frame2,text='''FULL DELUXE''',font=("Arial",9,"bold"),background="#ffffff",justify=LEFT)
var2 = IntVar()
var2.set(0)
Checkbutton2.place(relx=0.26, rely=0.72, relheight=0.11
                , relwidth=0.21)
Checkbutton2.configure(variable=var2)

# checkbutton widgets for guest general room        
Checkbutton3 = Checkbutton(Frame2,text='''GENERAL''',font=("Arial",9,"bold"),background="#ffffff")
var3 = IntVar()
var3.set(0)
Checkbutton3.place(relx=0.6, rely=0.6, relheight=0.11
                , relwidth=0.16)
Checkbutton3.configure(variable=var3)

# checkbutton widgets for guest joint room        
Checkbutton4 = Checkbutton(Frame2,text='''JOINT''',font=("Arial",9,"bold"),justify=LEFT,background="#ffffff")
var4 = IntVar()
var4.set(0)
Checkbutton4.place(relx=0.6, rely=0.71, relheight=0.11
                , relwidth=0.12)
Checkbutton4.configure(variable=var4)

# label widgets for guest payment method
Label7 = Label(Frame2,text='''CHOOSE PAYMENT METHOD''',font=("Arial",9,"bold"),background="#ffffff")
Label7.place(relx=0.3, rely=0.79, height=48, width=300)

# checkbutton widgets for guest payment by cash method
Checkbutton5 = Checkbutton(Frame2,text='''By cash''',font=("Arial",9,"bold"),background="#ffffff",justify=LEFT)
var5 = StringVar()
var5.set(0)
Checkbutton5.place(relx=0.250, rely=0.89, relheight=0.1
                                , relwidth=0.15)
Checkbutton5.configure(variable=var5)

# checkbutton widgets for guest payment by credit/debit card method
Checkbutton6 = Checkbutton(Frame2,text='''By credit/debit card''',font=("Arial",9,"bold"),background="#ffffff",justify=LEFT)
var6 = StringVar()
var6.set(0)
Checkbutton6.place(relx=0.600, rely=0.89, relheight=0.1
                                , relwidth=0.3)
Checkbutton6.configure(variable=var6)

# button widgets for submit guest data
Button5 = Button(Frame2,text='''SUBMIT''',font=("Arial",9,"bold"),background="#ffffff",pady="0")
Button5.place(relx=0.76, rely=0.66, height=53, width=86)
Button5.configure(command=submit_clicked)

# frame widgets
Frame3 = Frame(root,background="#ffffff",relief=GROOVE,borderwidth="2")
Frame3.place(relx=0.03, rely=0.78, relheight=0.2, relwidth=0.93)

# text widgets
Text1 = Text(root,background="#ffffff",width=994,wrap=WORD)
Text1.place(relx=0.03, rely=0.78, relheight=0.2, relwidth=0.93)

# To run use mainloop()    
root.mainloop()

