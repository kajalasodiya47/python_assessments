global customers
customers = {}

# define add_customer() function       
def add_customer(customer):
    # store customer details in customers key 'no' dictionary
    customers[customer['no']] = customer
    return customers

# define view_customer() function        
def view_customer(no):
    # use get() method to get customer details 
    res = customers.get(no)
    return res

# define view_all_customers() function
def view_all_customers():
    # get all customers details to use values() 
    return list(customers.values())

# define search_customer() function
def search_customer(keyword):
    # empty list
    result = []
    # use for loop
    for customer in customers.values():
        if keyword.lower() in customer['name'].lower() or str(keyword).lower() in str(customer['no']).lower():
             result.append(customer)
    return result

# define total_amount_bank() function
def total_amount_bank():
    # use sum(), values() dictionary method to get total amounts in bank
    total = sum(int(customer['balance']) for customer in customers.values())
    return total
         
