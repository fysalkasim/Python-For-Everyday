# x = 20  
# if x < 10:  
#     print("x is less than 10")  
# elif x < 30:  
#     print("x is between 10 and 30")  
# else:  
#     print("x is greater than or equal to 30")

string = "basketball and book"
import re
print(re.findall("b\w*k",string))