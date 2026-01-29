"""
Description:
    Returns days lapse between two dates or future date after start date + N days to add

Details:
    Ask the user for start date
    Ask the user if he wants to calculate days passed between two dates or future date after N days
    if the user wants to calculate future date, it asks for N days to add
    if the users wants to calculate days lapse between two dates it asks for end_date

    start_date, options, end_date, and days_to_add are provided by the user

    Output can be:
    future date: eg. 2026-02-28
    days passwed between two dates: eg. 28
"""

from datetime import datetime, timedelta

def get_valid_date():
    while True:
        # Ask the user for input in a specific format
        date_str = input("Enter a date in YYYY-MM-DD format (e.g., 2025-01-29): ")
        try:
            # Try to convert the string to a datetime object
            # %Y = 4-digit year, %m = 2-digit month, %d = 2-digit day
            date_object = datetime.strptime(date_str, "%Y-%m-%d").date()
            # If successful, break the loop and return the date object
            return date_object
        except ValueError:
            # If the format is incorrect, print an error and the loop continues
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_options():
    while True:
         options = input("""
What do you want to do ?
    1) Calculate future date after N days
    2) Calculate days lapse between two dates
? """)
         try:
             option = int(options)
             if (option >=1 and option <= 2):
                 return option
             else:
                 print("Enter a valid selection 1 or 2")
         except ValueError:
             print("Enter a valid selection 1 or 2")


def calculate_future_date():
    while True:
        try:
            days_to_add = int(input (f"How many days after {start_date} ? "))
            future_date = start_date + timedelta(days=days_to_add)
            return future_date
        except:
            print("Enter valid integer number")

def calculate_days_lapse():
    print(f"Enter end date > {start_date}")
    while True:
        end_date = get_valid_date()
        if (end_date > start_date):
            delta = end_date - start_date
            return delta.days
        else:
            print(f"Enter end date > {start_date}")

# Call the function to get the date
print("Enter start date: ")
start_date = get_valid_date()
option = get_options()
# map the inputs to the function blocks
switcher = {1 : calculate_future_date, 
            2 : calculate_days_lapse,
            }
result = switcher.get(option, lambda: "unknown")()
print(result)