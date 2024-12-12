# from datetime import datetime

# date_format="%d-%m-%"
# CATEGORY={"I":"Income","E":"Expence"}
# def get_date(prompt,allow_default=False):
#     date_str=input(prompt)
#     if allow_default and not date_str:
#         return datetime.today().strftime(date_format)
    
#     try:
#         valid_date=datetime.strptime(date_str,date_format)
#         return valid_date.strftime(date_format)
#     except ValueError:
#         print("invalid date format pls give dd-mm-yyyy")
#         return get_date(prompt,allow_default)

# def get_amount():
#     try:
#         amount=float(input("enter the amount :"))
#         if amount <=0:
#             raise ValueError("Amount must be a non-negative value")
#         return amount
#     except ValueError as e:
#         print(e)
    

# def get_category():
#     category=input("enter the category('I' for  income or 'E')")
#     if category in CATEGORY:
#         return CATEGORY[category]
#     print("invalid category ,please enter 'I' for income and 'E' for expense.")
#     return get_category()

    

# def get_description():
#     return input("enter a description (optional)")

from datetime import datetime

# Date format for parsing
date_format = "%d-%m-%Y"
CATEGORY = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        # Return today's date in the specified format
        return datetime.today().strftime(date_format)
    
    try:
        # Validate the input date and format it
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return get_date(prompt, allow_default)

# def get_amount():
    # try:
    #     # Prompt for the amount
    #     amount =(input("Enter the amount: ")).strip()
    #     amount=float(amount)
    #     if amount <= 0:
    #         raise ValueError("Amount must be a positive value.")
    #     return amount
    # except ValueError as e:
    #     print(e)
    #     return get_amount()
    

def get_amount():
    while True:
        try:
            # Prompt the user for the amount
            amount = input("Enter the amount: ").strip()
            
            # Check if the input is empty
            if not amount:
                print("Amount cannot be empty. Please enter a valid number.")
                continue
            
            # Convert the input to a float
            amount = float(amount)
            
            # Validate the amount is positive
            if amount <= 0:
                print("Amount must be a positive value.")
                continue
            
            # Return the valid amount
            return amount
        
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a numeric value for the amount.")

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORY:
        return CATEGORY[category]
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    # Prompt for an optional description
    return input("Enter a description (optional): ")
