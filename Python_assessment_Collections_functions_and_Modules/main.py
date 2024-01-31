# import modules
import banker
from customer import display_customer_details
from customer import withdraw_amt
from customer import deposite_amt
from customer import view_balance
from datetime import datetime

#Open the file "bank_management.txt" and append content to the file:
f = open("bank_management.txt","a")

# define a function display_banker_menu()
# shows banker manu
def display_banker_menu():
     print("\nWelcome to Banker's App")
     print("\n\t\tOperations Menu")
     print("\n\t\t\t1) Add Customer")
     print("\t\t\t2) View Customer")
     print("\t\t\t3) Search Customer")
     print("\t\t\t4) View All Customer")
     print("\t\t\t5) Total Amounts in Bank")
     print("\t\t\t6) Exit Banker")

# define a function is_valid_account_number()     
def is_valid_account_number(account_number):
     return account_number.isdigit() and len(account_number) == 10

# define a function is_valid_customer_name()
def is_valid_customer_name(customer_name):
     return customer_name.isalpha() and len(customer_name) > 0

# define a function is_valid_opening_balance()
def is_valid_opening_balance(opening_balance):
     try:
         balance = float(opening_balance)
         return balance >= 0
     except ValueError:
         return False

# define a function get_customer_details()
def get_customer_details():
     # get current date-time
     current_date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
     # Get user input for account creation
     while True:
         account_number = input("Enter account no : ")
         if is_valid_account_number(account_number):
             acc_no = account_number
             break
         else:
             print("Invalid account number. Please enter a valid 10-digit account number.")
     # Get user name for account creation
     while True:
         customer_name = input("Enter customer name : ")
         if is_valid_customer_name(customer_name):
             acc_name = customer_name   
             break
         else:
             print("Invalid name. Please enter a valid name with alphabetic characters.")
     # Get opening balance for account creation
     while True:
         opening_balance = input("Enter opening balance : ")
         if is_valid_opening_balance(opening_balance):
             acc_bal = opening_balance   
             break
         else:
             print("Invalid opening balance. Please enter a valid non-negative number.")
          
     return {'no': acc_no,'name': acc_name, 'balance': acc_bal, 'Opening Date' : current_date_time}     

# define a function banker_options()
def banker_options():
     status = True  
     while status:  
         # call the display_banker_menu()
         display_banker_menu()
         # enter operation
         op = input("\nEnter operation which you want to perform : ")
         # use ladder else-if statements to check the condition
         if op == '1':
             customer_details = get_customer_details()
             # call add_customer function() from the banker module
             cu = banker.add_customer(customer_details)
             keys_list = list(cu.items())
             # Get the last key
             last_key = keys_list[-1]
             #will overwrite any existing content
             f.write("\nCustomer added : "+str(last_key))
             print("Customer added successfully.")
         elif op == '2':
             # enter account number
             acc_no = input("Enter account number: ")
             # call view_customer function() from the banker module
             customer = banker.view_customer(acc_no)
             # call display_customer_details() function that shows the customer details
             display_customer_details(customer)
         elif op == '3':
             # enter search keyword
             keyword = input("Enter search keyword: ")
             # call search_customer() function from the banker module
             search_result = banker.search_customer(keyword)
             # use for loop
             for customer in search_result:
                 # call display_customer_details() function that shows the customer details
                 display_customer_details(customer)
         elif op == '4':
             cu_id = 100
             # empty dictionary
             all_cu = {}
             all_customers = banker.view_all_customers()
             # use for loop in all_customers
             for customer in all_customers:
                   cu_id = cu_id + 1  
                   all_cu[f'{cu_id}'] = {'name': customer['name'], 'balance' : customer['balance']
                                         ,'Opening Date': customer['Opening Date']}
                   # shows all the customer details
             print(all_cu)
         elif op == '5':
             # call the total_amount_bank() from the banker module
             ttl_amt = banker.total_amount_bank()
             print(f"Total Amount in Bank: {ttl_amt}")
         elif op == '6':
             # exit from the banker options
             break
         else: 
             # invalid choice
             print("Invalid choice. Please enter a number between 1 and 6.")
             continue
         more_op = input("Do you want to perform more opeartions press 'y' for yes and press 'n' for no : ")
         if more_op == 'y' or more_op == 'Y':
             status = True
         else:
             status = False
             break

# define a function display_customer_menu()   
def display_customer_menu():
     print("Welcome to Customer's App")
     print("\n\tOperations Menu")
     print("\n\n\t1)Withdraw Amount")
     print("\t2)Deposite Amount")
     print("\t3)View Balance")
     print("\t4)Exit Customer")

# define a function customer_options()
def customer_options():
     status = True  
     while status:  
         # call display_customer_menu() function
         display_customer_menu()
         # enter the operation
         ope = input("\nEnter operation which you want to perform : ")
         # use ladder else-if statements to check the condition
         if ope == '1':
             while True:
                # enter account number
                account_number = input("Enter account no : ")
                # call is_valid_account_number() function
                if is_valid_account_number(account_number):
                   acc_no = account_number
                   withdraw_amt(acc_no)  
                   break
                else:
                   print("Invalid account number. Please enter a valid 10-digit account number.")
         elif ope == '2':
             while True:
                # enter account number
                account_number = input("Enter account no : ")
                # call is_valid_account_number() function
                if is_valid_account_number(account_number):
                   acc_no = account_number
                   deposite_amt(acc_no)  
                   break
                else:
                   print("Invalid account number. Please enter a valid 10-digit account number.")
         elif ope == '3':
             while True:
                account_number = input("Enter account no : ")
                # call is_valid_account_number() function
                if is_valid_account_number(account_number):
                   acc_no = account_number
                   view_balance(acc_no)
                   break
                else:
                   print("Invalid account number. Please enter a valid 10-digit account number.")
         elif ope == '4':
             break
         else:
             # invalid choice
             print("Invalid choice. Please enter a number between 1 and 4.")
             continue
         more_op = input("Do you want to perform more opeartions press 'y' for yes and press 'n' for no : ")
         if more_op == 'y' or more_op == 'Y':
             status = True
         else:
             status = False
             break
          


# define a main function main()
def main():
     while True:   
         # shows menu
         print("\n\t\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
         print("\n\t\tSelect your role")
         print("\n\t\t\t1) Banker\n\t\t\t2) Customer\n\t\t\t3) Exit")
         # choose your role
         role = input("\nchoose your role : ")
         '''
         use ladder else if statements
         to check the condtion if entered role statisfy the condition than executes the code  
         '''
         if role == '1':
             # call banker_options() function
             banker_options()
         elif role == '2':
             # call customer_options() function
             customer_options() 
         elif role == '3':
             # exit from the bank application
             print("Thank you!!") 
             break
         else:
             # invalid choice
             print("Invalid choice. Please enter a number between 1 and 3.")  
          
main()
f.close()
        
