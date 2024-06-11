#CREATING TABLES
import sqlite3
import re
#import bcrypt
def create_tables() :
    db = sqlite3.connect("database_db.db")
    cursor = db.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS students (
        ID INTEGER PRIMARY KEY ,
        Name VARCHAR(255) NOT NULL,
        
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        Contact TEXT NOT NULL
        )
        '''
    )
    db.commit()
    
    cursor.execute (
        '''
        CREATE TABLE IF NOT EXISTS Buses (
        Bus_ID INTEGER PRIMARY KEY ,
        Bus_number VARCHAR(50) NOT NULL,
        model TEXT NOT NULL,
        capacity INT NOT NULL,
        operator_name VARCHAR(255) NOT NULL 
        )
        '''
    )

create_tables()

def booking_details(database) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()

        cursor.execute(
            '''
            INSERT OR IGNORE INTO students (ID,Name,Email,Password,Contact)
            VALUES(?,?,?,?,?)
            ''',(database['ID'],database['name'],database['email'],database['password'],database['contact'])
        )
        db.commit()
        
        cursor.execute(
            '''
            INSERT OR IGNORE INTO Buses (Bus_ID,Bus_number,model,capacity,operator_name)
            VALUES (?,?,?,?)
            ''',(details['bus_number'],details['model'],details['capacity'],details['operator_name'])
        )

def bus_input () :
    details = {}
    

    while True :
        bus_number = input("Enter bus number : ")
        if not bus_number :
            raise ValueError("Invalid input.")
        else :
            details['bus_number'] = bus_number
            break

    while True :
        model = input("Enter model of the bus : ")
        if not model :
            raise ValueError("Invalid Input. Please enter model .")
        else :
            details['model'] = model
            break

    while True :
        capacity = input("Enter capacity of bus : ")
        if not capacity.isdigit()  :
            raise ValueError("Invalid Input. Please enter an integer .")
        elif not capacity :
            raise ValueError("Invalid Input.")
        else :
            details['capacity'] = capacity
            break
    while True :
        operator_name = input("Enter operator name : ")
        if not operator_name :
            raise ValueError("Invalid Input.")
        else :
            details['operator_name'] = operator_name
            break

    return details
details = bus_input()




   


def user_input () :
        database = {}

        while True :
            id = input("Enter your Student  ID :  ")
            if not id.isdigit()  :
                raise ValueError("Invalid Input. Please enter your Student ID")
            else :
                database['ID'] = id
                break
        while True :
            name = input("Enter  Student's Name : ")
            if not name :
                raise ValueError("Invalid Input. Please enter student name : ")
            else :
                database['name'] = name
                break
        while True :
            email = input("Enter your email : ")
            pattern = r'^[a-zA-Z0-9.+_%+-]+@[a-zA-Z0-9+.-]+\.[a-zA-Z]*$'
            if re.match(pattern,email) :
                database['email'] = email
                break
            else :
                print("Invalid Input.")
        while True :
            password = input("Enter your password : ")
            if not password :
                raise ValueError("Invalid Input. Please enter your password : ")
            else :
                database['password'] = password
                break
        while True :
            contact = input("Enter your contact number example(254712345678) : ")
            if not contact :
                raise ValueError("Invalid Input. Please enter your contact number.")
            else :
                database['contact'] = contact
                break
        
        return database
database = user_input()
print("Information added successfully")
booking_details(database,details)

#STUDENT INFO
# studentID,name,username,email,password

#SCHOOLS PARTICIPATING IN THE BOOKING SYSTEM
#(nameofSchool,location,ContactInfo)

#INFO ON BUSES 
#(busID,buscompany,capacity,amenities)

#INFO ON TRIPS
#(bustrips,depature,arrival(TIMES),locations(depature,arrival),Price of ticket )


#BOOKINGS