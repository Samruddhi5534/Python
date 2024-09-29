class Student:
    def GetStudent(self):
        self.RollNo = int(input("\nEnter Student Roll No: "))
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Student Age: "))
        self.Gender = input("Enter Student Gender: ")

    def PutStudent(self):
        print("Student Roll No:", self.RollNo)
        print("Student Name:", self.Name)
        print("Student Age:", self.Age)
        print("Student Gender:", self.Gender)

class Test(Student):
    def GetMarks(self):
        self.MarkMar = int(input("Enter Marks of Marathi Subject: "))
        self.MarkHin = int(input("Enter Marks of Hindi Subject: "))
        self.MarkEng = int(input("Enter Marks of English Subject: "))

    def PutMarks(self):
        print("Marathi Marks:", self.MarkMar)
        print("Hindi Marks:", self.MarkHin)
        print("English Marks:", self.MarkEng)
        print("Total Marks:", self.MarkMar + self.MarkHin + self.MarkEng)

# Input for number of students
n = int(input("Enter How many students: "))

# List to hold student objects
lst = []

# Creating student objects and collecting data
for i in range(n):
    student = Test()  # Create a new instance of Test
    student.GetStudent()
    student.GetMarks()
    lst.append(student)  # Add the student object to the list

# Displaying details of each student
for j in range(n):
    print(f"\nDisplay Details of Student {j + 1}:")
    lst[j].PutStudent()
    lst[j].PutMarks()
