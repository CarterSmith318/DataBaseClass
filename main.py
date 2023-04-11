import Sqlserver as sql


server = "DESKTOP-UABTB2M"

database = "CarterSmithOnlineStore"

db = sql.SQLServer(server,database)

db.connect()

''' ///// '''

import Customer_generator as cg ## import generate_random_name, generate_random_number, generate_random_date, generate_random_birthdate, generate_random_phone_number

###first_name, last_name = cg.generate_random_name()
#number = cg.generate_random_number()
#date = cg.generate_random_date()
#birthdate = cg.generate_random_birthdate()
#phone_number = cg.generate_random_phone_number()

# print the generated data
# print(f"fName: {first_name}, lName: {last_name}, paymentInfo: {number}, customerJoinDate: {date}, phoneNo: {phone_number}, DoB: {birthdate}")

#headerArray = ['fName', 'lName', 'paymentInfo', 'customerID', 'customerJoinDate', 'phoneNo', 'DoB' ]

#inputArray = [ (first_name, last_name,number,date, birthdate, phone_number) ]

####print(inputArray)

headerArray = ['fName', 'lName', 'paymentInfo',  'customerJoinDate', 'phoneNo', 'DoB' ]
inputArray = []

for i in range(10000):
    first_name, last_name = cg.generate_random_name()
    number = cg.generate_random_number()
    date = cg.generate_random_date()
    birthdate = cg.generate_random_birthdate()
    phone_number = cg.generate_random_phone_number()

    inputArray.append((first_name, last_name,number,date, phone_number ,birthdate ))

print(inputArray)

db.send_data('customer', inputArray , columns= headerArray ) 