from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_user,course_id_name_user
from course_user_manager import add_course_user, search_course_user, view_course_users

def menu():
    
    print("\n\n\n***** Course number *****")
    print("***** Add course first *****")
    print(" (1) Object-Orientated Programming ")
    print(" (2) Reaserch Method ")
    print(" (3) Quantum Computing \n\n")
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Advanced search User by ID and name") # New feature
    print("7. Search User by course_id and name")
    print("\n==== Course Manager ====")
    print("Add your course blow....") 
    print("8. Add Course")
    print("9. Serach Course")
    print("10. View All Courses")
    #print("11. Delete Course by ID")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-10): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            course_id = input("Enter course id: ")
            add_user(name, email, course_id)
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
        
        # Activity 3 (search based on course_ID and user name)
        elif choice == '7':
            name = input("Enter name to search: ")
            course_id = input("Enter course id to serch: ")
            infos = course_id_name_user(name, course_id)
            for info in infos:
                print(info)
        
        # Enter the unit and course
        elif choice == '8':
            course = input("Enter your course: ")
            unit = input("Enter your unit: ")
            add_course_user(course,unit)
        
        # Search the courses based on name
        elif choice == '9':
            name = input("Enter the course to search: ").strip()
            names = search_course_user(name)
            for name in names:
                print(name)

        elif choice == '10':
            users = view_course_users()
            for user in users:
                print(user)
        #elif choice == '10':
            
            #delete_user()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
