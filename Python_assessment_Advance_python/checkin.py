# import modules
import tkinter
from tkinter import *
from subprocess import call
from hotel_management_database_connection import *

# create a class named CheckIn
class CheckIn:
    # dunder method
    def __init__(self,screen):
        self.screen = screen
        # set title and geometry for window
        self.screen.title("HOTEL MANAGEMENT")
        self.screen.geometry('700x500')
        self.screen.configure(bg="white")
        # call create_widgets() function
        self.create_widgets(self.screen)
        
    # member method
    def create_widgets(self,screen):
        self.screen = screen
        # Frame widgets
        self.Frame1 = Frame(self.screen)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="white")
        # Message widgets
        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(text='''YOU CLICKED ON''', font=("Arial", 15,"bold"))
        self.Message1.configure(width=496)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.52, rely=0.19, relheight=0.74, relwidth=0.07)
        self.Message2.configure(background="#ffffff")
        self.Message2.configure(text=''':''', font=("Arial", 15,"bold"))
        self.Message2.configure(width=66)

        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.57, rely=0.11, relheight=0.79, relwidth=0.35)
        self.Message3.configure(background="#ffffff")
        self.Message3.configure(text='''CHECK INN''', font=("Arial", 15,"bold"))
        self.Message3.configure(width=347)
        # Frame widgets
        self.Frame2 = Frame(self.screen)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.59, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(background="#ffffff")
        # Label widgets
        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.03, height=47, width=289)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(text='''ENTER YOUR NAME''',font=("Arial",9,"bold"))
        # message widgets
        self.Message4 = Message(self.Frame2)
        self.Message4.place(relx=0.41, rely=0.07, relheight=0.1, relwidth=0.05)
        self.Message4.configure(background="white")
        self.Message4.configure(text=''':''',font=("Arial",10,"bold"))
        # entry widgets
        self.Entry1 = Entry(self.Frame2)
        self.name=StringVar()
        self.Entry1.place(relx=0.47, rely=0.05,height=28, relwidth=0.33)
        self.Entry1.configure(background="white")
        self.Entry1.configure(textvariable=self.name)
        # button widgets 
        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05, height=30, width=43)
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''OK''',font=("Arial",10,"bold"))
        self.Button1.configure(command=self.chk_name)
        # label widgets
        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.032, rely=0.15, height=47, width=334)
        self.Label2.configure(background="white")
        self.Label2.configure(text='''ENTER YOUR ADDRESS''',font=("Arial",9,"bold"))
        # message widgets
        self.Message5 = Message(self.Frame2)
        self.Message5.place(relx=0.42, rely=0.18, relheight=0.12, relwidth=0.03)
        self.Message5.configure(background="white")
        self.Message5.configure(text=''':''',font=("Arial",10,"bold"))
        # Entry widgets
        self.Entry2 = Entry(self.Frame2)
        self.addr = StringVar()
        self.Entry2.place(relx=0.47, rely=0.18,height=28, relwidth=0.33)
        self.Entry2.configure(background="white")
        self.Entry2.configure(textvariable=self.addr)
        # button widgets
        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=30, width=43)
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''',font=("Arial",10,"bold"))
        self.Button2.configure(command=self.chk_add)
        # label widgets
        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.032, rely=0.28, height=47, width=329)
        self.Label3.configure(background="white")
        self.Label3.configure(text='''ENTER YOUR NUMBER''',font=("Arial",9,"bold"))
        # message widgets
        self.Message6 = Message(self.Frame2)
        self.Message6.place(relx=0.415, rely=0.3, relheight=0.09, relwidth=0.04)
        self.Message6.configure(background="white")
        self.Message6.configure(text=''':''',font=("Arial",10,"bold"))
        # Entry widgets
        self.Entry3 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry3.place(relx=0.47, rely=0.30,height=28, relwidth=0.33)
        self.Entry3.configure(background="white")
        self.Entry3.configure(textvariable=self.mobile)
        # button widgets
        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=30, width=43)
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''OK''',font=("Arial",10,"bold"))
        self.Button3.configure(command=self.chk_mo)
        # label widgets
        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.07, rely=0.40, height=44, width=260)
        self.Label4.configure(background="white")
        self.Label4.configure(text='''NUMBER OF DAYS''',font=("Arial",9,"bold"))
        # message widgets  
        self.Message7 = Message(self.Frame2)
        self.Message7.place(relx=0.41, rely=0.42, relheight=0.11, relwidth=0.04)
        self.Message7.configure(background="white")
        self.Message7.configure(text=''':''',font=("Arial",10,"bold"))
        # entry widgets
        self.Entry4 = Entry(self.Frame2)
        self.days=StringVar()
        self.Entry4.place(relx=0.47, rely=0.43, height=28, relwidth=0.33)
        self.Entry4.configure(background="white")
        self.Entry4.configure(textvariable=self.days)
        # button widgets
        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.91, rely=0.43, height=30, width=43)
        self.Button4.configure(background="#ffffff")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''OK''',font=("Arial",10,"bold"))
        self.Button4.configure(command=self.chk_day)
        # label widgets
        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.32, rely=0.5, height=48, width=296)
        self.Label5.configure(background="white")
        self.Label5.configure(text='''CHOOSE YOUR ROOM''',font=("Arial",9,"bold"))
        # checkbutton widgets
        self.Checkbutton1 = Checkbutton(self.Frame2)
        self.var1 = IntVar()
        self.var1.set(0)
        self.Checkbutton1.place(relx=0.28, rely=0.58, relheight=0.17
                , relwidth=0.14)
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''DELUXE''',font=("Arial",9,"bold"))
        self.Checkbutton1.configure(variable=self.var1)

        self.Checkbutton2 = Checkbutton(self.Frame2)
        self.var2 = IntVar()
        self.var2.set(0)
        self.Checkbutton2.place(relx=0.26, rely=0.72, relheight=0.11
                , relwidth=0.21)
        self.Checkbutton2.configure(background="#ffffff")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''FULL DELUXE''',font=("Arial",9,"bold"))
        self.Checkbutton2.configure(variable=self.var2)
        
        self.Checkbutton3 = Checkbutton(self.Frame2)
        self.var3 = IntVar()
        self.var3.set(0)
        self.Checkbutton3.place(relx=0.6, rely=0.6, relheight=0.11
                , relwidth=0.16)
        self.Checkbutton3.configure(background="#ffffff")
        self.Checkbutton3.configure(text='''GENERAL''',font=("Arial",9,"bold"))
        self.Checkbutton3.configure(variable=self.var3)
        
        self.Checkbutton4 = Checkbutton(self.Frame2)
        self.var4 = IntVar()
        self.var4.set(0)
        self.Checkbutton4.place(relx=0.6, rely=0.71, relheight=0.11
                , relwidth=0.12)
        self.Checkbutton4.configure(background="#ffffff")
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text='''JOINT''',font=("Arial",9,"bold"))
        self.Checkbutton4.configure(variable=self.var4)
        # label widgets
        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.3, rely=0.79, height=48, width=300)
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(text='''CHOOSE PAYMENT METHOD''',font=("Arial",9,"bold"))
        # checkbutton widgets
        self.Checkbutton5 = Checkbutton(self.Frame2)
        self.var5 = StringVar()
        self.var5.set(0)
        self.Checkbutton5.place(relx=0.250, rely=0.89, relheight=0.1
                                , relwidth=0.15)
        self.Checkbutton5.configure(background="#ffffff")
        self.Checkbutton5.configure(justify=LEFT)
        self.Checkbutton5.configure(text='''By cash''',font=("Arial",9,"bold"))
        self.Checkbutton5.configure(variable=self.var5)

        self.Checkbutton6 = Checkbutton(self.Frame2)
        self.var6 = StringVar()
        self.var6.set(0)
        self.Checkbutton6.place(relx=0.600, rely=0.89, relheight=0.1
                                , relwidth=0.3)
        self.Checkbutton6.configure(background="#ffffff")
        self.Checkbutton6.configure(justify=LEFT)
        self.Checkbutton6.configure(text='''By credit/debit card''',font=("Arial",9,"bold"))
        self.Checkbutton6.configure(variable=self.var6)
        # button widgets
        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.76, rely=0.66, height=53, width=86)
        self.Button5.configure(background="#ffffff")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''SUBMIT''',font=("Arial",9,"bold"))
        self.Button5.configure(command=self.submit_clicked)
        # frame widgets
        self.Frame3 = Frame(self.screen)
        self.Frame3.place(relx=0.03, rely=0.78, relheight=0.2, relwidth=0.93)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(background="#ffffff")
        # text widgets
        self.Text1 = Text(self.screen)
        self.Text1.place(relx=0.03, rely=0.78, relheight=0.2, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)
    # member method for run   
    def run(self,screen):
        self.screen = screen
        self.screen.mainloop()

# create a another class(child class)        
class PerformOperations(CheckIn):
    # member method for name validation 
    def chk_name(self):
            while True:
                # get the value of name field using get() method
                self.__k = str(self.name.get())
                __a = self.__k.isdigit()
                if len(self.__k) != 0 and __a != True:
                    self.Text1.insert(INSERT, "name has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid name""\n")
                    break
                
    # member method for address validation            
    def chk_add(self):
            while True:
                # get the value of address field using get() method
                self.__s = str(self.addr.get())
                __b = self.__s.isdigit()
                if len(self.__s) != 0 and __b != True:
                    self.Text1.insert(INSERT, "address has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid address""\n")
                    break
                
    # member method for mobile validation            
    def chk_mo(self):
             while True:
                # get the value of mobile field using get() method
                self.__h = str(self.mobile.get())
                if self.__h.isdigit() == True and len(self.__h) != 0 and len(self.__h) == 10:
                    self.Text1.insert(INSERT, "mobile number has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid mobile number""\n")
                    break
                
    # member method for day validation           
    def chk_day(self):
             while True:
                # get the value of days field using get() method 
                self.m = str(self.days.get())
                if self.m.isdigit() == True and len(self.m) != 0:
                    self.Text1.insert(INSERT, "days has been inputed""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "invalid input please input a valid days""\n")
                    break
                
    # member method
    def submit_clicked(self):
        # use get() method to get values
        self.__name = str(self.Entry1.get())
        self.__address = self.Entry2.get()
        self.__number = self.Entry3.get()
        self.days = self.Entry4.get()
        self.var1 = self.var1.get()
        self.var2 = self.var2.get()
        self.var3 = self.var3.get()
        self.var4 = self.var4.get()
        self.var5 = self.var5.get()
        self.var6 = self.var6.get()
        # dictionary for store values
        dict1 = {'name':self.__name,'address':self.__address,'number':self.__number,'days':self.days,'var1':self.var1,'var2':self.var2,'var3':self.var3,'var4':self.var4,'var5':self.var5,'var6':self.var6}
        # create Database class object database_ope
        database_ope = Database()
        # through database_ope obj call database() function
        database_ope.database(dict1)
        # through database_ope obj call access() function
        database_ope.access()
        self.Text1.insert(INSERT, "data added""\n")
        
# create a Tk() class object
root = Tk()
# create a child PerformOperations class object
perform_op = PerformOperations(root)
perform_op.run(root)
