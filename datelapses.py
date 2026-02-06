"""
Description:
    Returns days lapse between two dates 
    or future date after start date + N days to add 
    or future date after start date + N months to add 

Details:
    Ask the user for start date
    Ask the user if he wants to calculate days passed between two dates or future date after N days
    if the user wants to calculate future date after N days, it asks for N days to add
    if the users wants to calculate days lapse between two dates it asks for end_date
    if the user wants to calculate future date after N months, it asks for N months to add

    start_date, options, end_date, and days_to_add are provided by the user

    Output can be:
    future date: eg. 2026-02-28
    days passwed between two dates: eg. 28
"""

from datetime import datetime, timedelta, date
import calendar

def get_valid_date(prompt="Enter a date in YYYY-MM-DD format (e.g., 2025-01-29): "):
    """Get and validate a date input from the user."""
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_options():
    """Get and validate the user's operation choice."""
    while True:
        options = input("""
What do you want to do?
    1) Calculate future date after N days
    2) Calculate days lapse between two dates
    3) Calculate future date after N months
? """)
        try:
            option = int(options)
            if 1 <= option <= 3:
                return option
            print("Enter a valid selection 1-3 ")
        except ValueError:
            print("Enter a valid selection 1-3")

def get_positive_integer(prompt):
    """Get and validate a positive integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive integer")
        except ValueError:
            print("Enter a positive integer")

def add_months_no_delta(start_date, months):
    month = start_date.month - 1 + months
    year = start_date.year + month // 12
    month = month % 12 + 1
    # Adjust day if the new month has fewer days
    day = min(start_date.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)

def calculate_future_date_days(start_date):
    """Calculate a future date by adding N days to the start date."""
    days_to_add = get_positive_integer(f"How many days after {start_date}? ")
    return start_date + timedelta(days=days_to_add)

def calculate_days_lapse(start_date):
    """Calculate days lapsed between start date and end date."""
    print(f"Enter end date (must be after {start_date})")
    while True:
        end_date = get_valid_date("Enter end date in YYYY-MM-DD format: ")
        if end_date > start_date:
            return (end_date - start_date).days
        print(f"End date must be after {start_date}")

def calculate_future_date_months(start_date):
    """Calculate a future date by adding N months to the start date."""
    months_to_add = get_positive_integer(f"How many months after {start_date}? ")
    return add_months_no_delta(start_date, months_to_add)

def main():
    """Main function to run the date calculator."""
    print("Enter start date:")
    start_date = get_valid_date()
    option = get_options()

    # Execute the appropriate operation
    if option == 1:
        result = calculate_future_date_days(start_date)
    elif option == 2:
        result = calculate_days_lapse(start_date)
    else:
        result = calculate_future_date_months(start_date)

    print(result)

if __name__ == "__main__":
    main()