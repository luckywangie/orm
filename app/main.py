from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from  models import User, Category, Task, Base
import os
# SQLITE DB connection
engine =  create_engine("sqlite:///database.db",echo=False )
Session = sessionmaker(bind=engine)

session = Session()


# USER
def create_user():
    username = input("Enter your username : ")
    email = input("Enter your email    : ")

    user = User(username=username, email=email)
    session.add(user)
    session.commit()

    print(username, " created successfully!")


def fetch_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID : {user.id}  USERNAME : {user.username} EMAIL : {user.email}")


def fetch_user_by_id():
    user_id = input("Enter user ID to fetch: ")
    user = session.query(User).get(user_id)
    if user:
        print(f"ID:{user.id}, Username: {user.username}, Email: {user.email}, joined on: {user.joined_on}")
    else:
        print("user not found.")

def update_user():
    user_id = input("Enter user ID to update: ")
    user = session.query(User).get(user_id)
    if user:
        print(f"current Username: {user.username}, Email: {user.email},")
        new_username=input("Enter new username(press enter to skip):")
        new_email=input("Enter new email(press enter to skip):")

        if new_username:
            user.username=new_username
        if new_email:
            user.email=new_email

        session.commit()
        print("User updated successfully")
    else:
        print("User not found")

def delete_user():
    user_id=input("Enter user ID to delete:")
    user=session.query(User).get(user_id)
    if user:
        confirm=input(f"Are you sure you want to delete'{user.username}'?(y/n): ")
        if confirm.lower()=='y':
            session.delete(user)
            session.commit()
            print("User deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("User not found")






# Assignment
# Delete, Update, fetch single user

# CATEGORY
# Assignment
# ALL CRUD operations for category

# TASK
# CRUD 

# 

def main():
    while True:
        print("============TASK MANAGER=============")
        print("1. Create User ")
        print("2. List Users ")
        print("3. Fetch User by ID")
        print("4. Update User by ID")
        print("5. Delete User by ID")
        print("0. Exit ")
        choice = input("Enter your choice : ")

        if choice=="1":
            # os.system("clear")
            create_user()
        elif choice=="2":
            fetch_users()
        elif choice=="3":
            fetch_user_by_id()
        elif choice=="4":
            update_user()
        elif choice=="5":
            delete_user()  
        elif choice=="0":
            print("Bye! Bye!")
            break
        else:
            print("Invalid input! Try again!")


main()