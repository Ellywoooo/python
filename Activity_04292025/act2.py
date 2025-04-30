#Activity 2: Deadline 2 May - Simple Student Grading System Using classes
#Task: Create students, record their grades, and show results.
 
class Student:
    
    def __init__(self):
        
        print("\n\n-----------------------")
        print("Student grading system")
        print("-----------------------\n\n")
        
        #List of dictionary
        self.info = []
    
    #Input the student's name and score.
    def student_Info(self):
        
        self.name = input("Enter the student name: ")
        self.score = int(input("Enter the student's score: "))
        self.grade = ""
    
    #Calculate the grade based on the score.
    def student_Grade(self):
        if self.score >= 90:
            self.grade = "A"
        elif self.score >= 80:
            self.grade = "B"
        elif self.score >= 70:
            self.grade = "C"
        elif self.score >= 60:
            self.grade = "D"
        else:
            self.grade = "F"
        
        #Append name, score, and grade into dictionary list
        self.info.append({"name":self.name, "score":self.score, "grade":self.grade})

    #Show the results
    def student_result(self):
        
        print("\n\n-----------------------")
        print("   Students' results")
        print("-----------------------\n\n")
        for i in self.info:
            print(f"Name: {i['name']} Score: {i['score']} Grade: {i['grade']}")

#Create object
student = Student()

# Ask user to add student, if they choose no, it shows the all students' result
while True:
    add = input("Would you like to add student? (y) or (n) -> ")
    if add == "y":
        student.student_Info()
        student.student_Grade()
    elif add =="n":
        student.student_result()
        break
        