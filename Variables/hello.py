# print("hai python")
# print("OOPS")
# print("Data Science")


# #Collect the data from the user
# sjhda
# #convert the age into the tesultanat form
# skd
# #show the result

# age = input("Enter the age: ")   #str #int #float)
# print("your age is", age)

# print(type(age))
# after10_year = age + 10
# print(after10_year)



pin = 4368
count = 0
while True:    #condition always true
    num = int(input("Enter the number: "))
    count+= 1
    if count ==3:
        print("Account blocked")
        break
    if num == pin:
        print("Successfully logined")
        break
    else:
        print("Try again!!")

