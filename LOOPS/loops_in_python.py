# name = "Data"
# course = "Analytics"
# year = 2024
# print(name,course,sep="MMMMMMM",end=" ")
# year = 2024
# print(year)
# print(name,name,name,sep="\n")
# # print(name)
# # print(name)
# # print(name)
# list1 = [1,2,3,4,5,6]
# for i in list1:
#     print(i)

# name ="Data Analytics"
# for i in name:
#     print(i,end=" ")

# print(name*3)
# name ="Data Analytics"
# numbers = [1,2,3]
# for i in numbers:
#     print(name)

# thislist = list(range(1,100))
# print(thislist)

# name ="Data Analytics"
# for i in range(100):
#     print(name)
# limit = int(input("Enter the limit :"))
# for l in range(1,limit+1) :
#     print(l)

# sum = 0
# num = int(input("Enter the number"))
# for i in range(1,num+1):
#     sum += i
# print(sum)

# value = int(input("Enter the limit : "))
# i=0
# for i in range(1,value+1) :
#     i += i   
#     print(i)
# print("Sum =",i)
# res = 0
# value = int(input("Enter the limit : "))
# out =0
# for i in range(1,value+1) :
#     sum += i
# print("Sum =",sum)

numbers = [1, 2, 5, 6, 2, 4, 8, 3, 1, 5, 9, 7]
# print(sum(numbers))
# #
name = "FYSAL"
# print(name)
# for number in numbers:
#     print(number)

# foods = ["chaya", "Meals","Biriyani"]
# for i in foods:
#     print(i)
# print("Welcome to our hotel sir")
# foods = []
# for i in range(3):
#     food = input("Please order sir")
#     foods.append(food)

# for i in foods:
#     print(f"Your {i} is getting ready sir")

# print("Thank you for ordering")

# print("What do you want to eat:\nMenu:")
# food=["Tea","coffee","snacks"]
# for i in food:
#     print(i)

# orders = []
# for i in range(3):
#     order = input("What do you want sir: ")
#     orders.append(order)

# print(orders)

# *
# **
# ***
# ****

# for i in range(10):
#     print()
#     for j in range(i):
#         print("*",end='')
# for i in range(1,11):
#     print()
#     for j in range(i):
#         print("*",end='')

# print("apple","Banana",sep="",end='')
# print("Jack fruit",end="")

# fruits = ["Apple","Orange"]


# # print(len(fruits))
# for i  in range(len(fruits)):
#     for j in range(var2):
#         print(fruits[i])

# numbers= [1,2,5,6,2,4,8,3,1,5,9,7,10]
# for i in numbers :
#     print(i,end=" ")
#     j= numbers.index(i)
#     j+=1
#     if j < len(numbers) :
#         for j in numbers :
#             if i >= j :
#                 temp = i
#             else :
#                 temp = j   
# print("\nLargest number = ",temp)

# numbers=[1,2,5,6,2,4,8,3,1,5,9,7]
# print(max(numbers))
# # max_num=9
# # for i in numbers:
# #     if(i>max_num):
# #         max_num=i
# # print("\n maximum number is:",max_num)
# 

# create a list of fruits from users (it can be 1,2,3, or etc any number of elements),
# number of repeatition from user input
# print(each fruit as insructed by the user)

# limit = int(input("Enter the limit : "))
# a = 0
# b = 1
# for i in range(limit):
#     if i == 0:
#         print(a,end= " ") 
#     elif i == 1 :  
#         print(b,end= " ") 
#     else:
#         c = a + b
#         print(c,end= " ") 
#         a = b
#         b = c 
# count = int(input("Enter number of rows : "))
# for i in range(count,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# pyramid
# num=int(input("enter any number"))
# for i in range(0,num):
#     for j in range(num-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# mul=1
# n=int(input("Enter any num:")) 
# for i in range(1,n+1):
#     mul*=i
# print(f"The factorial of {n} is {mul}")

#1)Takes a list of numbers as input from the user and then separates and displays them as odd and even numbers
# inputing_string =(input("Enter the numbers (Separated by spaces):"))
# list_of_string = inputing_string.split()
# print(list_of_string)
# numbers = []
# for i in list_of_string:
#     numbers.append(int(i))
# print(numbers)

# odd=[]
# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers:",even)
# print("Odd Numbers:",odd)

# sentence=input("Enter a sentence:")
# vowels="aeiouAEIOU"
# vowels_count=0
# consonants_count=0

# for char in sentence:
#     if char.isalpha():
#         if char in vowels:
#             vowels_count += 1
#         else:
#             consonants_count += 1
# print("No of vowels:",vowels_count)
# print("No of consonants:",consonants_count)
# squares = []
# for i in range(1,11):
#     squares.append(i**2)

# print(squares)

# number = list(range(1,101))
# print(number)

# square = [i**2 for i in range(1,101)]
# print(square)
# cubes = [i**3 for i in range(1,10)]
# print(cubes)

#
# i=8
# while i>0:
#     print(i)
#     i -= 1


# i = 0
# while i<=10:
#     print("python")
#     i += 1

# i = 10
# while i>=0:
#     if i%2==0:
#         print(i)
#     i -= 1



# count = int(input("Enter number of rows : "))
# for i in range(0,count):  
#     for j in range(count,0,-1):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")    
#     print()

# break,continue,pass

# i = 0
# while i < 30:
#     if i == 10:
#         pass
#     print('Current number :', i)
#     i += 1
#else with while
# i=0
# while i<25:
#     if i==5:
#         break
#     print(i)
#     i=i+1
# else:
#     print(" no breaks")

    