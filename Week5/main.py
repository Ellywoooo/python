from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_user
from course_user_manager import add_course_user, search_course_user, view_course_users

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Advanced search User by ID and name") # New feature
    print("\n==== Course User Manager ====")
    print("7. Add course User")
    print("8. Serach course by name")
    print("9. View All Users")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            name = input("Enter name to search: ")
            user_id = int(input("Enter ID to serach: "))
            users = advanced_user(name, user_id)
            for user in users:
                print(user)
        
        # Enter the name and course
        elif choice == '7':
            name = input("Enter your name: ")
            unit = input("Enter your course: ")
            add_course_user(name,unit)
        
        # Search the courses based on name
        elif choice == '8':
            name = input("Enter the name to search: ").strip()
            names = search_course_user(name)
            for name in names:
                print(name)

        elif choice == '9':
            users = view_course_users()
            for user in users:
                print(user)
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
