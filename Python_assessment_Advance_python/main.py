# import modules
from tkinter import *
# import call through subprocess module
from subprocess import call

# call Tk class object
root = Tk()
# set title   
root.title("HOTEL MANAGEMENT")
# set geometry for window
root.geometry('700x500')
        
# create a function for checkin the guest
def click_check_in():
    # use call() throgh the subprocess module
    call(["python", "registration_form_tkinter.py"])

# create a function for exit
def exit_program():
    root.destroy()

# create a label widgets 
lbl = Label(root,text="WELCOME", font=('Arial', 20, 'bold'), fg="black")
lbl.pack()

# create a label widgets 
lbl = Label(root,text="HOTEL MANAGEMENT", font=('Arial', 22, 'bold'), fg="black")
lbl.place(x=350, y=80)

# create a label widgets 
lbl = Label(root,text="PYTHON TKINTER", font=('Arial', 25, 'bold'), fg="black")
lbl.place(x=350, y=140)

# create a label widgets 
lbl = Label(root,text="GUI", font=('Arial', 45, 'bold'), fg="black")
lbl.place(x=450, y=200)

# create a button widgets for check inn
button = Button(root,text="1.CHECK INN", font=('Times New Roman', 10), fg="black", width=30, height=2,
                        command=click_check_in)
button.place(x=100, y=80)

# create a button widgets for show guest list
button = Button(root,text="2.SHOW GUEST LIST", font=('Times New Roman', 10), fg="black", width=30, height=2)
button.place(x=100, y=130)

# create a button widgets for check out
button = Button(root,text="3.CHECK OUT", font=('Times New Roman', 10), fg="black", width=30, height=2)
button.place(x=100, y=180)

# create a button widgets for get info of any guest
button = Button(root,text="4.GET INFO OF ANY GUEST", font=('Times New Roman', 10), fg="black", width=30, height=2)
button.place(x=100, y=230)

# create a button widgets for exit
button = Button(root,text="5.EXIT", font=('Times New Roman', 10), fg="black", width=30, height=2,
                        command=exit_program)
button.place(x=100, y=280)

# To run use mainloop()
root.mainloop()    
        
