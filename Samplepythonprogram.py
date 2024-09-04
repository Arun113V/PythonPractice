

class Student:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

class School:
    def __init__(self):
        self.students = []

    def add_student(self,name,age,roll_no):
        student = Student(name, age, roll_no)
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll Number: {student.roll_no}")
            print("-----------------------")

    def edit_student(self,roll_no,new_name,new_age):
        for student in self.students:
            if student.roll_no == roll_no:
                student.name = new_name
                student.age = new_age
                print(f"Student {student.name} successfully updated")
                return
    def delete_student(self,roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully")
                return

school =School()

while True:
    choice = input("Enter your choice: \n1) Add Student \n2) Display list of students \n3) Edit the student detail \n4) Delete the student \n5) Exit \n")
    if choice == "1":
        name = input("Enter the name of the student:\t")
        age = input("Enter the age of the student:\t")
        roll_no = input("Enter the roll_no of the student:\t")
        school.add_student(name, age, roll_no)
    elif choice == "2":
        school.display_students()
    elif choice == "3":
        roll_no = input("Enter roll number which you want to edit")
        new_name = input("Enter new name for the student")
        new_age = input("Enter new age for the student")
        school.edit_student(roll_no,new_name,new_age)
    elif choice == "4":
        roll_no = input("Enter the roll number of the student to be deleted")
        school.delete_student(roll_no)
    elif choice == "5":
        break



