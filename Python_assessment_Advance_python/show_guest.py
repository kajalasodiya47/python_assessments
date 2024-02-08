# import modules
import tkinter
from tkinter import *
from hotel_management_database_connection import *

# create a class named ShowGusetList
class ShowGusetList:
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
          self.Message3.configure(text='''SHOW GUEST LIST''', font=("Arial", 15,"bold"))
          self.Message3.configure(width=347)
          # frame widgets
          self.Frame2 = Frame(self.screen)
          self.Frame2.place(relx=0.03, rely=0.18, relheight=0.69, relwidth=0.93)
          self.Frame2.configure(relief=GROOVE)
          self.Frame2.configure(borderwidth="2")
          self.Frame2.configure(background="#ffffff")
          # label widgets
          self.label1 = Label(self.Frame2)
          self.label1.place(relx=0.24, rely=0.09)
          self.label1.configure(text="Guest Name", font=('Arial', 12, 'bold'), fg="black")
          
          self.label2 = Label(self.Frame2)
          self.label2.place(relx=0.60, rely=0.09)
          self.label2.configure(text="Room Number", font=('Arial', 12, 'bold'), fg="black")
          # tet widgets
          self.guest_listbox = Text(self.screen,highlightthickness=0)
          self.guest_listbox.place(relx=0.03, rely=0.35,relheight=0.49, relwidth=0.92)
          # create Database class object database_ope
          database_ope = Database()
          # through database_ope obj call show_guest() function and show all guest details
          value = database_ope.show_guest()
          for row in value:
            self.guest_listbox.insert(END, f"\t\t\t{row[0]} \t\t\t\t{row[1]}\n")


# create a Tk() class object
root = Tk()
show_guest_list = ShowGusetList(root)

