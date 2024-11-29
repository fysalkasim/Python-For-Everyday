# fileptr = open(r"OCTOBER\File Handling\firstfile.txt","r")
# if fileptr:
#     print("file is opened successfully")
# else:
#     print("file not found")
# with open(r"OCTOBER\File Handling\firstfile.txt","r") as f:
#     print(f.read())

# fileptr = open(r"OCTOBER\File Handling\firstfile.txt", "r")
# print(fileptr.tell())
# print(fileptr.read())
# print(fileptr.tell())
# overwriting the content to the file
# fileptr.write("Again adding elements using a")
# fileptr.close()
# print(fileptr.read())
# for i in fileptr:
#     print(i)
# closing the opened the file
# fileptr.close()


# mytxt = open(r"C:\Users\CHROMIUM\Desktop\Python For Everyday\File Handling\file.txt",'r')
# if mytxt:
#     print("file is opened successfully")
# else:
#     print("file not found")
# mytxt.close()

# with open(r"C:\Users\CHROMIUM\Desktop\Python For Everyday\File Handling\file.txt","r") as mytxt:
#     content = mytxt.read()
#     print(content)

# fileptr = open(r"C:\Users\CHROMIUM\Desktop\Python For Everyday\File Handling\file.txt", "r")
# print(fileptr)
# fileptr = open(r"C:\Users\CHROMIUM\Desktop\Python For Everyday\File Handling\xfile.txt","x")
# print(fileptr)
# if fileptr:
#     print("File created successfully")
# overwriting the content to the file
# print(fileptr.tell())
# # print(fileptr.seek(0))
# print(fileptr.read())
# closing the opened the file
# for i in fileptr:
#     print(i,end="")
# line1 = fileptr.readline()
# line2 = fileptr.readline()
# line3 = fileptr.readline()
# line4 = fileptr.readline()
# print(line1)
# print(line2,end="")
# print(line3)
# print(line4)

# print(fileptr.readlines())
# fileptr.close()

# list1 = [1,2,3,4,5,6]
# list2 = [9,8,7,1,3,1]
# acv = (zip(list1,list2))
# print(acv)

# x = 5
# if x > 15:
#     print("x is greater than 15")
# else:
#     print("x is between 5 and 15")

# x = 10
# if x > 5:
#     print("A")
# elif x > 7:
#     print("B")
# else:
#     print("C")


x = 10
if x > 5:
    print("Greater than 5")
if x > 8:
    print("Greater than 8")
if x > 12:
    print("Greater than 12")
else:
    print("Equal or less than 12")

x = 10
if x > 5:
    print("Hello")
elif x > 8:
    print("Hi")
else:
    print("Hey")