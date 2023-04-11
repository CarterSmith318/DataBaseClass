import random
import string
import datetime

def generate_random_name():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=8))
    return (first_name, last_name)

def generate_random_number():
    number = ''.join(random.choices(string.digits, k=19))
    return number

def generate_random_date():
    year = random.randint(1907, 2010)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day).strftime('%Y-%m-%d')

def generate_random_birthdate():
    year = random.randint(1907, 2010)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day).strftime('%Y-%m-%d')

def generate_random_phone_number():
    area_code = ''.join(random.choices(string.digits, k=3))
    first_three = ''.join(random.choices(string.digits, k=3))
    last_four = ''.join(random.choices(string.digits, k=4))
    return f"({area_code}) {first_three}-{last_four}"



first_name, last_name = generate_random_name()
number = generate_random_number()
date = generate_random_date()
birthdate = generate_random_birthdate()
phone_number = generate_random_phone_number()


'''
print(f"fName: {first_name}")
print(f"lName: {last_name}")
print(f"paymentInfo: {number}")
print(f"customerJoinDate: {date}")
print(f"phoneNo: {phone_number}")
print(f"DoB: {birthdate}")
OLD FORMATT
'''
'''

print(f"{first_name},{last_name},{number},{date},{phone_number},{birthdate}")

'''
#print(f"fName: {first_name}, lName: {last_name}, paymentInfo: {number}, customerJoinDate: {date}, phoneNo: {phone_number}, DoB: {birthdate}")
