# # names = ["Reethu","Sreelekshmi","Sreekutty","Salu"]

# # age = [10,12,14,16]

# # print(type(names))
# # print(type(age))

# # print(names)
# # print(age)

# # print(names[-1])

# # names = ["Reethu","Sreelekshmi","Sreekutty","Salu","Lekshmi"]

# # print(len(names))


# # course = "Data_Analytics"

# # print(list(course))

# # course = list(course)
# # print(course)

# # del names[-1]
# # print(names)



# # names = ["Reethu","Sreelekshmi","Sreekutty","Salu"]
# # print(sorted(names))
# # numbers = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]

# # print(numbers)
# # print(len(numbers))

# # numbers[2:7] = [10,11,21]
# # print(numbers)
# # print(len(numbers))

# # numbers.append(5)
# # print(numbers)


# #Use of membership operators (in, not in)

# # player_names = ["Rohit","Dhoni","Virat","Rahul","Bumrah"]

# # print("Rohit" in player_names)

# # print("sachin" in player_names)
# # player_names = ["Rohit","Dhoni","Virat","Rahul","Bumrah"]
# # print(player_names[1])

# # player_names[1] = "Sanju samson"
# # print(player_names)

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # print(thislist)
# # # thislist[1:3] = ["Jack fruit", "watermelon"]
# # # print(thislist)
# # thislist[1:3] = ["Jack fruit", "watermelon", "Pappaya"]
# # print(thislist)
# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # thislist[1:3] = ["Jack fruit"]
# # print(thislist)
# # player_names = ["Rohit","Dhoni","Virat","Rahul","Bumrah"]
# # player_names.insert(1,"Sanju samson")
# # print(player_names)

# # basket = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # new_fruits = ["Jack fruit", "watermelon"]

# # basket.extend(new_fruits)
# # print(basket)

# # letters = "ABCDEFGHIJKL"

# # new_fruits.extend(letters)

# # print(new_fruits)

# # basket = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # print(basket)
# # basket.remove("kiwi")
# # print(basket)

# # basket = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # print(basket)
# # #remove the mango from basket

# # basket.pop()
# # print(basket)

# # list1 = [1,2,3,4]
# # list2 = [1,2,3,4]

# # list1.clear(5)
# # print(list1)



# # print("Hello world")
# # print("welcome to python programming")




# # fruit = ("Ap","ple")
# # print(list(fruit))

# # thislist = ["apple", "banana", "cherry"]
# # # thistuple = ("kiwi", "orange")
# # # print(type(thistuple))
# # thislist.insert(0,"thistuple")
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # thislist.remove("bana")
# # print(thislist)

# # thislist = "Python"
# # del thislist
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # for i in range(len(thislist)):
# #   print(thislist[i])


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# # thislist.sort(reverse=True)
# # print(thislist)


# # print(sorted(thislist))
# # print(thislist.sor)

# thislist = [1,2,3,4,5,6]
# mylist = thislist.copy()
# print(mylist)

# mylist.reverse()
# print(mylist)
# print(thislist)
# my_list = []

# for i in range(5):
#     my_list.insert(0,i)

# print(my_list)
# import re
# txt = "helo planet"
# x = re.findall("he.{3}o", txt)
# print(x)

# Assignment 342: Find Sequences Starting with “py” and Ending with “on”
# Write a Python program to find sequences in the string "python and pylon" that start with "py" and end with "on" using re.findall().
# Expected Output:
# ['python', 'pylon']

import re
string = "The scores were 12, 34, and 56"    
x = re.findall("[0-9][0-9]",string)
print(x)

