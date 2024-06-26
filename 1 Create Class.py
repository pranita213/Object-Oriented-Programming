# Author : Pranita Z 
# Create Class 
# A Class in Python is a blueprint for creating objects (instances).
# Class attributes are shared by all instances of the class.


class Student:
    name = "Student"  # Create class attribute


obj = Student()   # Create an instance of the Student class
print(obj)        # Print object's memory details
print(obj.name)   # Access and print the class attribute 'name' using the instance


obj1 = Student()   # Create another instance of the Student class
print(obj1)        # Print object's memory details
print(obj1.name)   # Access and print the class attribute 'name' using the instance

#Since name is a class attribute, it is shared by all instances of the Student class and thus can be accessed using the instance.