# import modules
from tkinter import *
# import database connection file for perform database operations
from hotel_management_database_connection import *

# call Tk class object
root = Tk()

# set title and geometry for window
root.title("Registration Form")
root.geometry('500x500')

# create a function for submit user data in database
def submit_clicked():
    # use get() method to get the all the entry widgets value 
    name = Entry1.get()
    contact = Entry2.get()
    email = Entry3.get()
    gender = var.get()
    city = clicked.get()
    state = clicked1.get()
    # ladder else-if
    if len(name) == 0 :
         label21.config(text="Please enter a username")
    elif len(contact) == 0:
         label31.config(text="Please enter a contact number")
    elif len(email) == 0:
         label41.config(text="Please enter a email address")
    elif len(gender) == 0:
         label51.config(text="Please select a gender")
    elif len(city) == 0:
         label61.config(text="Please select a city")
    elif len(state) == 0:
         label71.config(text="Please select a state")          
    else:
         # dictionary create 
         dict2 = {'name':name,'contact':contact,'email':email,'gender':gender,'city':city,'state':state}
         database1(dict2)

# label widgets
label1 = Label(root,text = '''Please enter details below''',font=("Arial",10,"bold"),background="orange")
label1.place(rely=0.03, height=47, width=500)

# label widgets for user name        
label2 = Label(root,text = '''Name *''',font=("Arial",10,"bold"))
label2.place(relx=0, rely=0.14, height=30, width=100)

# entry widgets for user name
Entry1 = Entry(root,background="white")
Entry1.place(relx=0.27, rely=0.14, height=30, width=200)

# label widgets
label21 = Label(root,text = "",fg="red")
label21.place(relx=0.3, rely=0.20, height=30, width=200)

# label widgets for user contact number 
label3 = Label(root,text = '''Contact *''',font=("Arial",10,"bold"))
label3.place(relx=0, rely=0.26, height=30, width=100)

# entry widgets for user contact number
Entry2 = Entry(root,background="white")
Entry2.place(relx=0.27, rely=0.26, height=30, width=200)

# label widgets
label31 = Label(root,text = "",fg="red")
label31.place(relx=0.3, rely=0.32, height=30, width=200)

# label widgets for user email address
label4 = Label(root,text = '''Email *''',font=("Arial",10,"bold"))
label4.place(relx=0, rely=0.38, height=30, width=100)

# entry widgets for user email address
Entry3 = Entry(root,background="white")
Entry3.place(relx=0.27, rely=0.38, height=30, width=200)

# label widgets
label41 = Label(root,text = "",fg="red")
label41.place(relx=0.3, rely=0.44, height=30, width=200)

# label widgets for user gender
label5 = Label(root,text = '''Gender *''',font=("Arial",10,"bold"))
label5.place(relx=0, rely=0.50, height=30, width=100)

# radiobutton widgets for user male gender
var = StringVar()
var.set(0)
Radiobutton1 = Radiobutton(root,text = '''Male''',font=("Arial",10,"bold"),variable=var,value=1)
Radiobutton1.place(relx=0.25, rely=0.50, width=100)

# radiobutton widgets for user female gender
Radiobutton2 = Radiobutton(root,text = '''Female''',font=("Arial",10,"bold"),variable=var,value=2)
Radiobutton2.place(relx=0.45, rely=0.50, width=100)

# lable widgets 
label51 = Label(root,text = "",fg="red")
label51.place(relx=0.3, rely=0.56, height=30, width=200)

# label widgets for user city
label6 = Label(root,text = '''City *''',font=("Arial",10,"bold"))
label6.place(rely=0.62, height=30, width=100)

# dropdown widgets for user city
options = [ 
    "Ahmedabad", 
    "Rajkot", 
    "Surat", 
    "Vadodara"
        ] 
clicked = StringVar()
drop1 = OptionMenu(root , clicked , *options )
drop1.configure(background="white")
drop1.place(relx=0.28, rely=0.62, width=200)

# lable widgets
label61 = Label(root,text = "",fg="red")
label61.place(relx=0.3, rely=0.68, height=30, width=200)

# label widgets for user state
label7 = Label(root,text = '''State *''',font=("Arial",10,"bold"))
label7.place(rely=0.74, height=30, width=100)

# dropdown widgets for user state       
options1 = [ 
    "Gujarat", 
    "MP", 
    "UP"
      ] 
clicked1 = StringVar()
drop2 = OptionMenu(root , clicked1 , *options1 )
drop2.configure(background="white")
drop2.place(relx=0.28, rely=0.74, width=200)

# lable widgets
label71 = Label(root,text = "",fg="red")
label71.place(relx=0.3, rely=0.80, height=30, width=200)

# button widgets for submit user data
Button1 = Button(root,text='''Register''',font=("Arial",10,"bold"),background="orange")
Button1.place(relx=0.33,rely=0.86, height=33, width=150)
Button1.configure(command=submit_clicked)

# To run use mainloop()
root.mainloop()
    
