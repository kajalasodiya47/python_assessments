# import modules
import tkinter
from tkinter import *
from hotel_management_database_connection import *

# define a class named RegistrationForm
class RegistrationForm:
    # dunder method
    def __init__(self,screen):
        self.screen = screen
        # set title and geometry for window
        self.screen.title("Registration Form")
        self.screen.geometry('500x500')
        # call the create_widgets() function
        self.create_widgets(self.screen)
        # for run use mainloop()
        self.screen.mainloop()
        
    # member method
    def submit_clicked(self):
        # use get() method to get the all the entry widgets value and for name, contact and email to use private access specifier
        self.__name = str(self.Entry1.get())
        self.__contact = str(self.Entry2.get())
        self.__email = str(self.Entry3.get())
        self.gender = str(self.var.get())
        self.city = str(self.clicked.get())
        self.state = str(self.clicked1.get())
        # ladder else-if
        if len(self.__name) == 0 :
             self.label21.config(text="Please enter a username")
        elif len(self.__contact) == 0:
             self.label31.config(text="Please enter a contact number")
        elif len(self.__email) == 0:
             self.label41.config(text="Please enter a email address")
        elif len(self.gender) == 0:
             self.label51.config(text="Please select a gender")
        elif len(self.city) == 0:
             self.label61.config(text="Please select a city")
        elif len(self.state) == 0:
             self.label71.config(text="Please select a state")          
        else:
             # dictionary create 
             dict2 = {'name':self.__name,'contact':self.__contact,'email':self.__email,'gender':self.gender,'city':self.city,'state':self.state}
             # create a another file Database class object here
             databbase_op = Database() 
             databbase_op.database1(dict2)

            
    # another member method    
    def create_widgets(self,root):
        self.root = root
        # label widgets
        self.label1 = Label(self.root)
        self.label1.place(rely=0.03, height=47, width=500)
        self.label1.configure(text = '''Please enter details below''',font=("Arial",10,"bold"),background="orange")
        
        self.label2 = Label(self.root)
        self.label2.place(relx=0, rely=0.14, height=30, width=100)
        self.label2.configure(text = '''Name *''',font=("Arial",10,"bold"))
        # entry widgets
        self.Entry1 = Entry(self.root)
        self.Entry1.place(relx=0.27, rely=0.14, height=30, width=200)
        self.Entry1.configure(background="white")
        # label widgets
        self.label21 = Label(self.root)
        self.label21.place(relx=0.3, rely=0.20, height=30, width=200)
        self.label21.configure(text = "",fg="red")

        self.label3 = Label(self.root)
        self.label3.place(relx=0, rely=0.26, height=30, width=100)
        self.label3.configure(text = '''Contact *''',font=("Arial",10,"bold"))
        # entry widgets
        self.Entry2 = Entry(self.root)
        self.Entry2.place(relx=0.27, rely=0.26, height=30, width=200)
        self.Entry2.configure(background="white")
        # label widgets
        self.label31 = Label(self.root)
        self.label31.place(relx=0.3, rely=0.32, height=30, width=200)
        self.label31.configure(text = "",fg="red")

        self.label4 = Label(self.root)
        self.label4.place(relx=0, rely=0.38, height=30, width=100)
        self.label4.configure(text = '''Email *''',font=("Arial",10,"bold"))
        # entry widgets
        self.Entry3 = Entry(self.root)
        self.Entry3.place(relx=0.27, rely=0.38, height=30, width=200)
        self.Entry3.configure(background="white")
        # label widgets
        self.label41 = Label(self.root)
        self.label41.place(relx=0.3, rely=0.44, height=30, width=200)
        self.label41.configure(text = "",fg="red")

        self.label5 = Label(self.root)
        self.label5.place(relx=0, rely=0.50, height=30, width=100)
        self.label5.configure(text = '''Gender *''',font=("Arial",10,"bold"))

        self.var = StringVar()
        self.var.set(0)
        # radiobutton widgets
        self.Radiobutton1 = Radiobutton(self.root)
        self.Radiobutton1.place(relx=0.25, rely=0.50, width=100)
        self.Radiobutton1.configure(text = '''Male''',font=("Arial",10,"bold"),variable=self.var,value=1)

        self.Radiobutton2 = Radiobutton(self.root)
        self.Radiobutton2.place(relx=0.45, rely=0.50, width=100)
        self.Radiobutton2.configure(text = '''Female''',font=("Arial",10,"bold"),variable=self.var,value=2)
        # lable widgets
        self.label51 = Label(self.root)
        self.label51.place(relx=0.3, rely=0.56, height=30, width=200)
        self.label51.configure(text = "",fg="red")

        self.label6 = Label(self.root)
        self.label6.place(rely=0.62, height=30, width=100)
        self.label6.configure(text = '''City *''',font=("Arial",10,"bold"))
        # dropdown widgets
        self.options = [ 
           "Ahmedabad", 
           "Rajkot", 
           "Surat", 
           "Vadodara"
           ] 
        self.clicked = StringVar()
        # dropdown widgets
        self.drop1 = OptionMenu(self.root , self.clicked , *self.options )
        self.drop1.configure(background="white")
        self.drop1.place(relx=0.28, rely=0.62, width=200)
        # lable widgets
        self.label61 = Label(self.root)
        self.label61.place(relx=0.3, rely=0.68, height=30, width=200)
        self.label61.configure(text = "",fg="red")

        self.label7 = Label(self.root)
        self.label7.place(rely=0.74, height=30, width=100)
        self.label7.configure(text = '''State *''',font=("Arial",10,"bold"))
        
        self.options1 = [ 
           "Gujarat", 
           "MP", 
           "UP"
           ] 
        self.clicked1 = StringVar()
        # dropdown widgets
        self.drop2 = OptionMenu(self.root , self.clicked1 , *self.options1 )
        self.drop2.configure(background="white")
        self.drop2.place(relx=0.28, rely=0.74, width=200)
        # lable widgets
        self.label71 = Label(self.root)
        self.label71.place(relx=0.3, rely=0.80, height=30, width=200)
        self.label71.configure(text = "",fg="red")
        # button widgets
        self.Button1 = Button(self.root)
        self.Button1.place(relx=0.33,rely=0.86, height=33, width=150)
        self.Button1.configure(background="orange")
        self.Button1.configure(text='''Register''',font=("Arial",10,"bold"))
        self.Button1.configure(command=self.submit_clicked)

# crate a Tk() class object
root = Tk()
registration_form = RegistrationForm(root)    
