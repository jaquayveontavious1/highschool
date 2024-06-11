import sqlite3
def create_tables () :
    db = sqlite3.connect("database_db.db")
    cursor = db.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS buses (
        Bus_ID INTEGER PRIMARY KEY,
        Bus_number VARCHAR(50) NOT NULL,
        model TEXT NOT NULL,
        capacity INT NOT NULL,
        operator_name VARCHAR(255) NOT NULL
        )
        '''
    )
    db.commit()

def booking_dets (details) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO buses (Bus_ID,Bus_number,model,capacity,operator_name)
            VALUES(?,?,?,?,?)
            ''',(details['Bus_ID'],details['bus_number'],details['model'],details['capacity'],details['operator_name']
           )
        )


def bus_input () :
    details = {}
    while True :
        bus_ID = input("Enter ID of Bus : ")
        if not bus_ID.isdigit() :
            raise ValueError("Invalid. Please enter an integer! ")
        elif not bus_ID :
            raise ValueError("Invalid. Please enter a Bus ID")
        else :
            details['Bus_ID'] = int(bus_ID)
            break
    while True :
        bus_number = input("Enter bus number : ")
        if not bus_number  :
            raise ValueError("Invalid Input. Please enter a bus number !!")
        elif not bus_number.isdigit() :
            raise ValueError("Invalid Input. Please enter a valid integer!! ")
        else :
            details['bus_number'] = int(bus_number)
            break
    while True :
        model = input("Enter model of bus : ")
        if not model :
            raise ValueError("Enter model of the bus!!")
        else :
            details['model'] = model
            break
    while True :
        capacity = input("Enter Capacity of the Bus : ")
        if not capacity :
            raise ValueError("Invalid Input!!")
        elif not capacity.isdigit() :
            raise ValueError("Invalid. Enter a valid integer!!")
        else :
            details['capacity'] = int(capacity)
            break
    while True :
        operator_name = input("Enter name of company for bus : ")
        if not operator_name :
            raise ValueError("Invalid. Please enter am operator name!!")
        else :
            details['operator_name'] = operator_name
            break
    
    return details
create_tables()
details = bus_input()
print("Information successfully added!")
booking_dets(details)
