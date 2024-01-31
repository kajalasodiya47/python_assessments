# import banker module
import banker

# define display_customer_details() function
def display_customer_details(customer):
    # to check customer exists or not to use if-else statement
    if customer:
        print("Customer Details:")
        print(f"Customer Name: {customer['name']}")
        print(f"Customer Account Balance: {customer['balance']}")
    else:
        print("Customer not found.")

# define withdraw_amt() function
def withdraw_amt(no):
    # get customer details through entered account number from the banker module
    res = banker.customers.get(no)
    # to check that customer exists or not to use if-else statement
    if res:
        print("The name of the account holder : ",res['name'])
        print("Current account balance : ",res['balance'])
        # enter withdraw amount
        with_amt = input("Enter withdraw amount : ")
        # use if-else statement to check current balance is greater than entered withdraw amount
        if int(res['balance']) > int(with_amt) :
            # minus the withdraw amount from the current balance
            res['balance'] = int(res['balance']) - int(with_amt)
            print("Withdraw successfully!!")
            print("Balance in your account : ",res['balance'])
        else:
            print("Sorry!!Insufficient Avilable Balance in your account")
    else:
       print("Account does not exist!!")

# define deposite_amt() function
def deposite_amt(no):
    # get customer details through entered account number from the banker module
    res = banker.customers.get(no)
    # to check that customer exists or not to use if-else statement
    if res:
        print("The name of the account holder : ",res['name'])
        print("Current account balance : ",res['balance'])
        # enter deposite amount
        dep_amt = input("Enter deposite amount : ")
        # plus the deposite amount with the current balance
        res['balance'] = int(res['balance']) + int(dep_amt)
        print("Deposited successfully!!")
        print("Balance in your account : ",res['balance'])
    else:
        print("Account does not exist!!")

# define view_balance() function
def view_balance(acc_no):
    # get customer details through entered account number from the banker module
    res = banker.customers.get(acc_no)
    # to check that customer exists or not to use if-else statement
    if res:
        print("The name of the account holder : ",res['name'])
        print("Account number : ",res['no'])
        print("Balance in your account : ",res['balance'])
    else:
        print("Account does not exist!!")   
