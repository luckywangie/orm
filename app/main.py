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


#fetch
def fetch_user_by_id():
    user_id = input("Enter user ID to fetch: ")
    user = session.query(User).get(user_id)
    if user:
        print(f"ID:{user.id}, Username: {user.username}, Email: {user.email}, joined on: {user.joined_on}")
    else:
        print("user not found.")

# UPDATE
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

# DELETE
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


#Category
def create_category():
    name=input("Enter category name.")
    existing=session.query(Category).filter_by(name=name).first()
    if existing:
        print("Category already exists.")
        return
    
    category=Category(name=name)
    session.add(category)
    session.commit()
    print("Category created successfully.")


def list_category():
    categories=session.query(Category).all()
    if not categories:
        print("No categories found.")
    for cat in categories:
        print(f"ID: {cat.id}, Name: {cat.name}")


def fetch_category_by_id():
    cat_id=input("Enter category ID to fetch")
    category=session.query(Category).get(cat_id)
    if category:
        print(f"ID: {category.id}, Name: {category.name}")
    else:
        print("Category not found.")


def update_category():
    cat_id=input("Enter category ID to update:")
    category=session.query(Category).get(cat_id)
    if category:
        print(f"current_name:{category.name}")
        new_name=input("Enter new name:")
        if new_name:
            category.name=new_name
            session.commit()
            print("category updated successfully.")
        else:
            print("Name not entered, not updated.")
    else:
        print("category not found.")


def delete_category():
    cat_id=input("Enter category ID to delete:")
    category=session.query(Category).get(cat_id)
    if category:
        confirm=input(f"Are you sure you want to delete '{category.name}'?(y/n): ")
        if confirm.lower()=='y':
            session.delete(category)
            session.commit()
            print("category deleted.")
        else:
            print("Delete cancelled.")
    else:
        print("category not found.")

#Task
def create_task():
    title=input("Task title: ")
    description=input("Task description: ")
    user_id=input("User_ID: ")
    category_id=input("Category ID: ")
    task=Task(title=title,description=description,user_id=user_id,category_id=category_id)
    session.add(task)
    session.commit()
    print("Task created.")
    return task

def list_tasks():
    tasks=session.query(Task).all()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(f"ID: {t.id}, Title: {t.title}, Description: {t.description}")

def fetch_task_by_id():
    task_id=input("Enter task ID to fetch:")
    task=session.query(Task).get(task_id)
    if task:
        print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}")
    else:
        print("Task not found.")

def update_task():
    task_id=input("Enter task ID to update:")
    task=session.query(Task).get(task_id)
    if task:
        title=input("Task title: ")
        description=input("Task description: ")
        task.title=title
        task.description=description
        session.commit()
        print("Task updated.")
    else:
        print("Task not found.")

def delete_task():
    task_id=input("Enter task ID to delete:")
    task=session.query(Task).get(task_id)
    if task:
        session.delete(task)
        session.commit()
        print("Task deleted.")
    else:
        print("Task not found.")



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
        print("6. create category")
        print("7. List All categories")
        print("8. Fetch single category by ID")
        print("9. update category")
        print("10. Delete category")
        print("11. Create Task")
        print("12. List All Tasks")
        print("13. Fetch single task by ID")
        print("14. Update Task")
        print("15. Delete Task")
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
        elif choice=="6":
            create_category() 
        elif choice=="7":
            list_category()
        elif choice=="8":
            fetch_category_by_id()
        elif choice=="9":
            update_category()
        elif choice=="10":
            delete_category() 
        elif choice=="11":
            create_task()
        elif choice=="12":
            list_tasks()
        elif choice=="13":
            fetch_task_by_id()
        elif choice=="14":
            update_task()
        elif choice=="15":
            delete_task()
        elif choice=="0":
            print("Bye! Bye!")
            break
        else:
            print("Invalid input! Try again!")


main()