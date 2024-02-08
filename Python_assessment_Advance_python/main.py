# import modules
import tkinter
from tkinter import *
from subprocess import call

# define a class named HotelManagement
class HotelManagement:
    # dunder method
    def __init__(self,screen):
        self.screen = screen
        # set title and geometry for window
        self.screen.title("HOTEL MANAGEMENT")
        self.screen.geometry('700x500')
        
    # member method
    def create_widgets(self,screen):
        self.screen = screen
        # create a label widgets
        self.lbl = Label(self.screen,text="WELCOME", font=('Arial', 20, 'bold'), fg="black")
        self.lbl.pack()

        self.lbl = Label(self.screen,text="HOTEL MANAGEMENT", font=('Arial', 22, 'bold'), fg="black")
        self.lbl.place(x=350, y=80)

        self.lbl = Label(self.screen,text="PYTHON TKINTER", font=('Arial', 25, 'bold'), fg="black")
        self.lbl.place(x=350, y=140)

        self.lbl = Label(self.screen,text="GUI", font=('Arial', 45, 'bold'), fg="black")
        self.lbl.place(x=450, y=200)

        # create a button widgets
        self.button = Button(self.screen,text="1.CHECK INN", font=('Times New Roman', 10), fg="black", width=30, height=2,
                        command=self.click_check_in)
        self.button.place(x=100, y=80)

        self.button = Button(self.screen,text="2.SHOW GUEST LIST", font=('Times New Roman', 10), fg="black", width=30, height=2,
                        command=self.show_guest_list)
        self.button.place(x=100, y=130)

        self.button = Button(self.screen,text="3.CHECK OUT", font=('Times New Roman', 10), fg="black", width=30, height=2,
                        command=self.check_out)
        self.button.place(x=100, y=180)

        self.button = Button(self.screen,text="4.GET INFO OF ANY GUEST", font=('Times New Roman', 10), fg="black", width=30, height=2,
                        command=self.get_guest_info)
        self.button.place(x=100, y=230)

        self.button = Button(self.screen,text="5.EXIT", font=('Times New Roman', 10), fg="black", width=30, height=2,
                        command=self.exit_program)
        self.button.place(x=100, y=280)
        # To run use mainloop()
        self.screen.mainloop()    
        
# define a another class  
class HotelManagementOps(HotelManagement):

    # define another member method     
    def click_check_in(self):
        # Add the logic for check-in here
        # use call() throgh the subprocess module
        call(["python", "checkin.py"])

    def show_guest_list(self):
        # Add the logic for showing the guest list here
        # use call() throgh the subprocess module
        call(["python", "show_guest.py"])

    def check_out(self):
        # Add the logic for check-out here
        # use call() throgh the subprocess module
        call(["python", "check_out.py"])

    def get_guest_info(self):
        # Add the logic for getting guest info here
        # use call() throgh the subprocess module
        call(["python", "get_info_guest.py"])

    def exit_program(self):
        # Add the logic for exit here
        self.screen.destroy()

if __name__ == "__main__":
    # create a Tk class object
    root = Tk()
    # create a child HotelCreateWidgets class object
    hotel_management_ops = HotelManagementOps(root)
    hotel_management_ops.create_widgets(root)
    
