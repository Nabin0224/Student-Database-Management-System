def remove_student(students, student_id):

    """ This function is intended to remove student form the system """
    
    if student_id in students:
        del students[student_id]

    else:
        print(f"The student with student id {student_id} doesnot exists")

def add_student(students, student_id, name):
    
    """ This function is indented to add student into the system """
    
    if student_id in students:
        print(f"The student id {student_id} already exists")

    else:
        students[student_id] = { 'name' : name, 'grade' : []}
        print(f"The student with id {student_id} is added succesfully!\n")


def add_grade(students, student_id, grade):

    """ This function is intented to add grade of student into the system """

    if student_id in students:
        students[student_id]['grade'].append(grade)
        print(f"The grade added to the student with id {student_id} succesfully!\n")
    
    else:
        print(f"Student with id no {student_id} doesnot exists")

def calculate_average(students, student_id):
    
    """ This function is used to calclate the average of the student """
    
    if student_id in students:
        sum1 = 0
        avg = 0
        sum1 = sum(students[student_id]['grade'])
        len1 = len(students[student_id]['grade'])
        avg = sum1 / len1
        print(avg)

    else:
        print(f"The student with id {student_id} doesnot exists")


def list_all_students(students):

    """ This function is used to list all the students and their data from the system """
    if not students:
        print("No data!!")

    else:
        for key, value in students.items():
            print("ID:" , key,value)

# empty dictionary initization 
print("\n \n")
students = {}

while(True):

        print("This is Student_Grade_Management_System\n")
        print("Enter '1' to add student into the data base")
        print("Enter '2' to remove a student")
        print("Enter '3' to Add Grade")
        print("Enter '4' Calulate Average Grade")
        print("Enter '5' to List All the Students")
        print("Enter '6' to Exit")
        choice = int(input("Your Choice : "))
        
        if choice == 1 :
            name = input("Enter name of student ")
            student_id = int(input("Enter id of student "))
            add_student(students, student_id ,name)
            print("----------------------------------")

        if choice == 2 :
            student_id = int(input("Enter the id of the student "))
            remove_student(students, student_id)
            print("----------------------------------")

        if choice == 3 :
            student_id = int(input("Enter the id of the student "))
            grade = int(input("Enter the grade of the student "))
            add_grade(students, student_id, grade)
            print("----------------------------------")

        if choice == 4 :
            student_id = int(input("Enter the id "))
            calculate_average(students, student_id)
            print("----------------------------------")

        if choice == 5 :
            list_all_students(students)
            print("----------------------------------")


        if choice == 6 :
            break
            print("----------------------------------")

