# Author : Pranita Z 
#__init__ method in Python is a special method used for initializing newly created objects. 
# __init__  is also known as the constructor method in object-oriented programming.

class Student:
    def __init__(self):
        print("__init__ called")  #Special constructor as called automatically
        self.name = "Default Name"  # Default value for the student's name
        self.age = 18  # Default value for the student's age

# Create an instance of the Student class
student1 = Student()   #__init__ is called automatically 

# Access default attributes
print(student1.name)  
print(student1.age)   

# Modify the attributes
student1.name = "Pranita"
student1.age = 20

# Access modified attributes
print(student1.name)  
print(student1.age)   

# Create an instance of the another Student class
student2 = Student() 
print(student2.name)  
print(student2.age)