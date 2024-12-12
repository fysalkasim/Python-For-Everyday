# print()
# input()
# type()
# list()
# set()
# dict()
# tuple()
# int()
# str()
# sorted()
# len()
# range()

# print(list(range(int(input()))))
# del
# print()

# string = """"Welcome to the world of
# python"""
# def functionname():
#     """docstring"""
#     print("Just called my function")

# functionname()
# f(x) = x*5

# x = parameter 
# f(5)
# 5 is an argument to the parameter x
# 25
# def double(number):
#     """Gives the double of the given number"""
#     return number*2
# def triple(num):
#     return num*3
# name = inpu

# def fun(a,b,c):
#     return a*b*c
# taking values from the user
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# def addition(num1, num2):
#     return num1+num2
# # printing the sum of a and b
# print("Sum = ", addition(a, b))


# def show(name,age,id):
#     print(name)

# show()
# print("python","C++",sep ="******",end="")
# print("java")


# def favorite_movie(movie,year=2014):
#     print(f"{movie} is my favorite movie in {year}")

# favorite_movie(year=2015,movie="Intersteller")


# def printme(*names):
#     for i in names:
#         print(i)

# printme("john","David","smith","nick")

# def information(name,**info):
#     print(name)
#     print(inf)

# information("fysal",place="Kaloor",job="Data analyst",k)

# year = 2025
# def show_year():
#     global year
#     year = 2024 #local
#     print(year)

# show_year()
#  #global
# year = 2026
# print(year)

# Assignment 71:
# Write a function named get_formatted_name() that takes three parameters: first_name, 
# last_name, and an optional middle_name. The function should return the full name, neatly formatted, 
# with the first and last name always included, and the middle name only if it's provided. Then, use this function

# def get_formatted_name():
#     first_name = input("Enter the first name: ")
#     last_name = input("Enter the middle name: ")
#     print(f"you are {first_name} {last_name}")

# # get_formatted_name()

# def create_student_profile(first_name, last_name,**userinfo):
#     # print(f"I think you are name is {first_name} {last_name}")

#     userinfo.update({"First_name":first_name,"last_name":last_name})
#     print(userinfo)


# create_student_profile("fysal","kasim",place="Kaloor")

# s = sum((1,2),100)
# print(s)



# name = "hey "
# # print(dir(name))

# list1 = ["Fysal",2,3,4,5,6,7]
# list2 = [80,6,7,8,9,10]
# print(dict(zip(list1,list2)))

# print(dict([("A","C")]))

# str = ["apple","orange","banana"]
# # Calling function
# sorted1 = sorted(str) # sorting string
# # Displaying result
# print(sorted1)
# x = 5
# print('x =', x, '= y')

# print(round(10.066,2))
# \
# 7

# mydoubler = myfunc(2)
# print(mydoubler(2))

# mytripller = myfunc(3)
# print(mytripller(2))



#function definition
# def hello():
#     return "hello world...bye"

# # function calling
# msg = hello()

# print(int(input("Enter number")))

# def sum(a, b):
#     return a + b

# sum(2,5)

# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)
# nameAge("Fysal")


def student(firstname, lastname, course = "Data science"):
    #  print(firstname, lastname, 'studies in', standard, 'Standard')
    print('Your are ',firstname,lastname,"right!","And you are studying",course)
# student("Fysal","Kasim")
# student(lastname="Kasim",firstname="Fysal")

# student("Fysal","kasim")

# def printme(*names):
#     for name in names:
#         print(name)

# printme("john","David","smith","nick")

# name = "Data"

# def printname():
#     name = "Python"
#     print(name)

# printname()

# print(name)


# x = [1,2,3,4]
# z = list(map(lambda a :a**2,x))
# print(z)

# name = set()
# print(type(name))







# print()
# type()
# len()
# sorted()
# int()
# input()


# f(x) = x+5*2-15/53

# f(5) = 10
# f(6) = 11

def hello():
    return "hello world...bye"

# print(type(tuple(list(range(int(len(input())))))))


hello()

# print("Hello world!!","Python","is great",)


# def welcome(name,year, course= "Data"):
#     print(f"Your name is {name} and you are living in {year} and you are studying {course}!!!")

# welcome("Hridya",2025)

# def printme(*names):    #tuples
#     for i in names:
#         print(i)

# printme("john","Hridya")


# printme(10,20)

# def food(**kwargs):
#     for i,j in kwargs.items():
#         print(j)
# # food(a="Apple")
# food(fruits="Orange", Vagitables="Carrot")