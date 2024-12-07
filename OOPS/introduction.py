# class Employee:
#     id = 10
#     name = "John"
#     def display(self):
#         print(f"{self.id}, {self.name}")
#     # Creating a emp instance of Employee class

# emp = Employee()
# # print(emp.id)
# # print(emp.name)
# emp.display()

# class Employee:
#     def __init__(self,name,id):
#         self.id = id
#         self.name = name
#     def display(self):
#         print(f"{self.id}, {self.name}")

# # emp1 = Employee()
# emp2 = Employee("David", 102)
# # accessing display() method to print employee 1 information
# print(emp2.id)

# emp2.display()


# course = "Data science"
# print(type(course))    #functions #methods class functions

# year = 2024


# .count, .index,


# class Employee:
#     id = 10
#     name = "Devansh"
#     def display(self):
#         print(self.id,self.name)
# e=Employee()
# del e.name
# e.display()

# class Student:
#     # Constructor - non parameterized
#     def __init__(self):
#         print("This is non parametrized constructor")
#     def show(self,name,id):
#         print("Hello",name)
# student = Student()
# student.show("John",12)


# class Student:
#     """A class about students and their addresses"""
#     def __init__(self,name,id,age):
#         self.name = name
#         self.id = id
#         self.age = age
#     def display_details(self):
#         print("Name:%s, ID:%d, age:%d" % (self.name,self.id,self.age))
# s = Student("John",101,22)
# print("Doc:",s.__doc__)
# print("Dict:",s.__dict__)
# print("Module:",s.__module__)
# print("Name:",Student.__name__)
# print("Base:",Student.__bases__)

# m = "dasd"
# print(isinstance(m,int))


# num = 10
# num2 = 0

# if num2 == 0:
#     pass
# else:
#     print(num/num2)  #Exception

# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     c = a/b
# except (ZeroDivisionError,ValueError):
#     print("Happy!!")

# else:
#     print("result:",c)

# while True:
#     try:
#         age = int(input("Enter the age:"))
#         if(age<18):
#             raise ZeroDivisionError("U18")
#         else:
#             print("the age is valid")
#             break
#     except Exception as E:
#         print("The age is not valid",E)

# even = []
# for i in range(1,25):
#     if i%2==0:
#         even.append(i)
# print(even)


