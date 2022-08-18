import sys
from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import Session


# constants
base = declarative_base()
conn_info = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432,
    "dbname": "test"
}


class People(base):  
    __tablename__ = 'people'

    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)


def get_url(user:str, password:str, host:str, port:int, dbname:str) -> str:
    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    return url


def instructions() -> None:
    print("\n\nKEYS ->\n")
    print("CREATE : create and add data to the database.")
    print("READ : view the database.")
    print("UPDATE : update/ change existing data in the database.")
    print("DELETE : delete data in the database.")
    print("QUIT : close program.")
    print("INSTRUCTIONS : view these instructions again.\n\n")


def get_user_key() -> str:
    key = input("Enter key: ")
    key = key.upper()

    return key


def execute_operations(key:str, session) -> None:
    if key == "CREATE":
        create(session)
    elif key == "READ":
        read(session)
    elif key == "UPDATE":
        update(session)
    elif key == "DELETE":
        delete(session)
    elif key == "INSTRUCTIONS":
        instructions()
    elif key == "QUIT":
        sys.exit()
    else:
        print("Not a key.\n\n")


def get_data(session) -> list:
    data = []

    new_first_name = input("Enter first name: ")
    new_first_name = new_first_name.capitalize()
    data.append(new_first_name)

    new_last_name = input("Enter last name: ")
    new_last_name = new_last_name.capitalize()
    data.append(new_last_name)

    while True:
        new_dob = input("Enter date of birth (yyyy-mm-dd): ")
        if len(new_dob) != 10:
            print("Enter an acceptable date of birth (yyyy/mm/dd).")
        else:
            break
        
    data.append(new_dob)

    return data


def create(session) -> None:
    create_data = get_data(session)


    new_first_name, new_last_name, new_dob = create_data[0], create_data[1], create_data[2]

    people = session.query(People)

    for person in people:
        if new_first_name == person.first_name and new_last_name == person.last_name:
            print(f"{new_first_name} {new_last_name} already in database.")
            print("\n")
            return
        else:
            new_person = People(first_name = new_first_name, last_name = new_last_name, dob = new_dob)
            print("\n")
            session.add(new_person)
            session.commit()
            return 

    new_person = People(first_name = new_first_name, last_name = new_last_name, dob = new_dob)
    print("\n")
    session.add(new_person)
    session.commit()
    return 


def read(session) -> None:
    people = session.query(People)
    for person in people:
        print(person.first_name, person.last_name, person.dob)
        
    print("\n")


def update(session) -> None:
    print("To update a persons data, start by entering the first and last name of the person you wish to update.")

    prev_data = get_data(session)
    prev_first_name, prev_last_name = prev_data[0], prev_data[1]

    people = session.query(People)
    for person in people:
        if person.first_name == prev_first_name and person.last_name == prev_last_name:
            print("Now update the person with their new data.")

            updated_data = get_data(session)
            updated_first_name, updated_last_name, updated_dob = updated_data[0], updated_data[1], updated_data[2]

            person.first_name = updated_first_name
            person.last_name = updated_last_name
            person.dob = updated_dob
            
            print("Successfully updated")
            print("\n")
            session.commit()
            return

    print(f"{prev_first_name} {prev_last_name} not in database...")
    print("Update failed.")
    print("\n")


def delete(session) -> None:
    print("To delete a persons data, enter their first and last names.")

    delete_data = get_data(session)
    delete_first_name, delete_last_name = delete_data[0], delete_data[1]

    print("Are you sure you want to delete this data?")
    confirm = input("Enter y/n: ")
    confirm = confirm.lower()

    if confirm == "y":
        people = session.query(People)
        for person in people:
            if person.first_name == delete_first_name and person.last_name == delete_last_name:
                print("Data deleted.")
                print("\n")
                session.delete(person)
                session.commit()
                return
        print("Persons data does not exist")
        print("\n")
        return
    else:
        print("\n")
        return


def main() -> None:
    url = get_url(**conn_info)
    engine = create_engine(url)
    session = Session(engine)
    base.metadata.create_all(engine)

    instructions()
    while True:
        key = get_user_key()
        execute_operations(key, session)


if __name__ == "__main__":
    main()