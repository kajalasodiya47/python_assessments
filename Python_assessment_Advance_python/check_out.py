# import modules
import tkinter
from tkinter import *
from hotel_management_database_connection import *

# create a class named CheckOut
class CheckOut:
      # dunder method
      def __init__(self,screen):
          self.screen = screen
          # set title and geometry for window
          self.screen.title("HOTEL MANAGEMENT")
          self.screen.geometry('700x500')
          self.screen.configure(bg="white")
          # call create_widgets() function
          self.create_widgets(self.screen)
          # To run use mainloop()
          self.screen.mainloop()
          
      # member method
      def create_widgets(self,screen):
          self.screen = screen
          # frame widgets
          self.Frame1 = Frame(self.screen)
          self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
          self.Frame1.configure(relief=GROOVE)
          self.Frame1.configure(borderwidth="2")
          self.Frame1.configure(background="white")
          # message widgets
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
          self.Message3.configure(text='''CHECK OUT''', font=("Arial", 15,"bold"))
          self.Message3.configure(width=347)
          # frame widgets
          self.Frame2 = Frame(self.screen)
          self.Frame2.place(relx=0.03, rely=0.18, relheight=0.50, relwidth=0.93)
          self.Frame2.configure(relief=GROOVE)
          self.Frame2.configure(borderwidth="2")
          self.Frame2.configure(background="#ffffff")
          # label widgets
          self.Label1 = Label(self.Frame2)
          self.Label1.place(relx=0.22, rely=0.08, relheight=0.20, relwidth=0.43)
          self.Label1.configure(background="#ffffff")
          self.Label1.configure(text='''ENTER THE ROOM NO.''',font=("Arial",12,"bold"))
          # message widgets
          self.Message4 = Message(self.Frame2)
          self.Message4.place(relx=0.58, rely=0.12, relheight=0.1, relwidth=0.05)
          self.Message4.configure(background="white")
          self.Message4.configure(text=''':''',font=("Arial",12,"bold"))
          # entry widgets
          self.Entry1 = Entry(self.Frame2)
          self.name=IntVar()
          self.Entry1.place(relx=0.67, rely=0.10,height=28, relwidth=0.06)
          self.Entry1.configure(background="white")
          # button widgets
          self.Button1 = Button(self.Frame2)
          self.Button1.place(relx=0.50, rely=0.45, height=45, width=95)
          self.Button1.configure(background="#ffffff")
          self.Button1.configure(pady="0")
          self.Button1.configure(text='''CHECK OUT''',font=("Arial",10,"bold"))
          self.Button1.configure(command=self.chk_out)
          # frame widgets
          self.Frame3 = Frame(self.screen)
          self.Frame3.place(relx=0.03, rely=0.78, relheight=0.2, relwidth=0.93)
          self.Frame3.configure(relief=GROOVE)
          self.Frame3.configure(borderwidth="2")
          self.Frame3.configure(background="#ffffff")
          # text widgets
          self.Text1 = Text(self.screen)
          self.Text1.place(relx=0.03, rely=0.70, relheight=0.28, relwidth=0.93)
          self.Text1.configure(background="white")
          self.Text1.configure(width=994)
          self.Text1.configure(wrap=WORD)

# create a another class(child class)
class CheckOutOpe(CheckOut):          
      # member method
      def chk_out(self):
          # get the value using get() method  
          self.a = self.Entry1.get()
          # create Database class object database_ope
          database_ope = Database()
          # through database_ope obj call check_room() function 
          res = database_ope.check_room(self.a)
          if res:
             for val in res:   
               self.Text1.insert(END, f"Valid room number\nThank You {val} for Visting us.")
          else:
               self.Text1.insert(END, "Invalid room number.")
               
# create a Tk() class object               
root = Tk()
check_out_ope = CheckOutOpe(root)
