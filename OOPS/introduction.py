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

class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name
    def display(self):
        print(f"{self.id}, {self.name}")

# emp1 = Employee()
emp2 = Employee("David", 102)
# accessing display() method to print employee 1 information
print(emp2.id)

emp2.display()