import datetime

def calculate_age(year, month, day):
    birth_date = datetime.date(year, month, day)
    current_date = datetime.date.today()
    
    if birth_date > current_date:
        return "Invalid birth date. Please enter a valid past date."
    
    age = current_date - birth_date
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    
    return f"You are {years} years, {months} months, and {days} days old."

def main():
    year = int(input("Enter birth year (YYYY): "))
    month = int(input("Enter birth month (MM): "))
    day = int(input("Enter birth day (DD): "))
    
    result = calculate_age(year, month, day)
    print(result)

if __name__ == "__main__":
    main()
