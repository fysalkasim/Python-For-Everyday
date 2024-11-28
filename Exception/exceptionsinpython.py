# name = "python"
# print(name)
# print(10/0)

# # print(name+5)

# thislist = [1,2,3,4,5,6]
# print(thislist[9])

# # try:
# #     a = int(input("Enter a:"))
# #     b = int(input("Enter b:"))
# #     c = a/b
# #     print("result:",c)
# #     print("hi..")
# # except Exception as ex:
# #     print("There is an error in the input",ex)
# # # except ValueError:
# # #     print("Can't divide with unknown value")

# # print("outside exception")


# try:
#     age = int(input("Enter the age:"))

#     if(age!=18):
#         raise ValueError
#     else:
#         print("the age is valid")
# except Exception:
#     print("The age is not valid")
#     print(Exception)

# print("outside exception")

# from math import statss

# print("hell world")

# number = int(input("Enter the number: "))

# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     c = a/b
# except ZeroDivisionError as Z:
#     print("Enter naother value on the second number: ",Z)
# except ValueError:
#     print("VAl")
# except NameError:
#     print("NAM")

# else:
#     print("result:",c)
# print("outside exception")


# while True:
#     try:
#         a = int(input("Enter a:"))
#         b = int(input("Enter b:"))
#         c = a/b
#         print(c)
#         break
    
#     # Using exception object with the except statement
#     except Exception as e:
#         print("Try again with different number: ")

# while True:
#     try: 
#         n = int(input("Please Enter an Integer: "))
#         break
#     except ValueError:
#         print(" The Integer You entered is not valid! Please try again…")
# print("You successfully entered an Integer!")

# try:
#      num = int(input("Enter a positive integer: "))
#      if(num <= 0):
#         # we can pass the message in the raise statement
#         raise ValueError("That is  a negative number!")

# except Exception as e:
#      print(e)
# else:
#      print(num)
