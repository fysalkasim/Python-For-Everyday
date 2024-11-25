# a = ("John", "Charles", "Mike","Rocky")
# b = ("Jenny", "Christy", "Monica", "Vicky")
# print(dict(zip(a,b)))

# help(zip())


def functionname():
    """Creating a function that welcomes to python"""
    return "Welcome to python"

# functionname()

# pp = functionname()
# print(pp)

# inp = input("enter the name")
# name = "python"
# print(name)

#required arguments
# print(list(range(len(str(input())))))
# print(len())

# def add(num1,num2):
#     return num1+num2

# def square(num):
#      print(num **2)
# square(add(1,2))
# print(add(1,2,3))
# def add():
#     return 5+4

# print(add())
# print(add(1))

# def favc(name,colour):
#     return name+colour

# print(favc("fysal","blue"))

# print(favc(1,2))

# print(favc({1,2,3},{1,4,5}))




# favc("fysal","blue")

# favc("blue","fysal")
# def favc(name,colour,year):
#     print(f"{name}'s favorite colour is {colour}")
#     print(year)

# favc(colour="blue",name="fysal",2024)
# favc("fysal","blue",year=2024)

# def power(number,power=2):
#     print(number**power)


# power(power=3,number=2)

# def printme(*names):
#     for name in names:
#         print(name)
# printme()

# def group(members,*names):
#     print("There will be",members,"of members")
#     for i in names:
#         print(i)

# group(5,"fysal","sree","reethu","shalu")


# def student(name,**info):
#     # print(name)
#     info.update({"name":name})
#     print(info)

# student("fysal",Blood="o+",home="kaloor")

# def print_message():
#     message = "hello !! I am going to print a message." # the variable message is local to the function itself
#     print(message)

# print_message()
# print(message)
# sum=0
# def calculate(*numbers):
#     # sum=0
#     # for number in numbers:
#         # sum = sum +number
#     print("The sum is",sum)

# calculate(1,2,3,4,5)

# # thislist = 
# print(sum([1,2,3,4,5,6]))


# calculate(10,20,30) #60 will be printed as the sum
# # print("Value of sum outside the function:",sum) # 
# 0 will be printed  Output:

# def greeting(name):
#     global msg
#     msg = "Welcome to the world of python"
#     print(f"{name}! {msg}")

# greeting("smec")
# print(msg)


# prime or not
# num = int(input("Enter a positive integer greater than 1 : "))
# def prime_check(n):
#     cnt=0
#     if n<=1:
#         print(f"{n} is not a prime number")
#     else:
#         for i in range(2,n+1):
#             if n%i == 0:
#                 cnt = cnt + 1          
#         if cnt>=2:
#             print(f"{n} is NOT a prime number")  
#         else:
#             print(f"{n} is a prime number")                    
# prime_check(num)

# rows = int(input("Enter the number of rows : "))
# for i in range(1,rows+1):
#     for j in range(i):
#         print(i,end= " ")
#     print()

# factors=[]
# number=int(input("enter the number:"))
# if(number==2):
#     print("{number} is prime number")
# for i in range(number+1):
#     if(i>=1 and number%i==0):
#         factors.append(i)
#     # print(factors)
# if(len(factors)==2):
#     print(f"the number {number} is prime number")
# elif(len(factors)>2):
#     print(f"the {number} is not prime")



# def palindrome():
#     word = input("Enter a word:")
#     str_rev=word[::-1]
#     if str_rev==word:
#         print(f"The word \"{word}\" is a palindrome")
#     else:
#         print(f"The word \"{word}\" is not a palindrome")
# palindrome()

# def oddnum():
#     n=int(input("Enter the number"))
#     for i in range(n):
#         if i%2!=0:
#             print(i)
# oddnum()


# n=int(input("Enter the number:"))
# def oddnum(n):
#     for i in range(n):
#         if i%2!=0:
#             print(i)
# oddnum(n)

# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(3, 5)
# print(a[x])


# ss = 12

# print(int(ss))



# list of numbers
# list = [1,2,3,4,5]
# listIter = iter(list)
# # prints '1'
# print(next(listIter))
# # # prints '2'
# print(next(listIter))
# # # prints '3'
# print(next(listIter))
# # prints '4'
# print(next(listIter))
# # prints '5'
# print(next(listIter))


# thislist = [1,2,3,4,5]
# print(thislist)

# # Calling function
# # att = dir()
# # Displaying result
# # print(dir(thislist))

# val = "python") # string object
# val2 = id() # integer object
# val3 = id([25,336,95,236,92,3225]) # List object
# # Displaying result
# print(val)
# print(val2)
# print(val3)


# str1 = "Hell"
# str2 = "Hell"

# print(id(str1),id(str2))


#  for integers
# print(round(10.02451545,1))




    
