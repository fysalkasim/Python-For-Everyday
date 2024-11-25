# thistring = "Welcome to Data Analytics"
# print(thistring.title())
# print(thistring)
# thisstring = "hi all this is going to be fun"
# print(thisstring.title())
# print(thisstring.capitalize())
# print(thisstring.upper())
# thisstring = thisstring.upper()
# print(thisstring)
# print(thisstring.lower())
# thisstring = "hi we are going to use rstrip() "
# print(len(thisstring.rstrip()))  #contains 31 element
# print(len(thisstring)) #contains 32 element

# thisstring = "   hi we are going to use lstrip()"
# print(len(thisstring.lstrip())) #contains 31 element
# print(len(thisstring)) #contains 34 element

# thisstring = "   Hi all  we are using strip() function  "
# print(len(thisstring.strip())) #contains 37 element
# print(len(thisstring)) #contains 42 element
# thisstring = "We are using replace method"
# print(thisstring)
# print(thisstring.replace("using","used"))
# print(thisstring)   #no change in orginal string

# names = "SALU SREEKUTTY SREELEKSHMI REETHU"
# print(names.split(" "))  #printing each names using split method using whitspace as separtor

# thisstring = "Use of count index and find"
# print(thisstring.find("U"))
# print(thisstring.index("U"))
# print(thisstring.count("U"))

# thistring = "We are using join method in string"
# print(thistring.join("12345"))

# thisstring = "Hi all we are going to use startswith"
# print(thisstring.startswith("Hi"))

# thisstring = "Hi all we are going to use endswith"
# print(thisstring.endswith("Hi"))

# print(thisstring.endswith("th"))

# thisstring = "Hi all we are going to use isalpha"
# print(thisstring.isalpha())

# thisstring = "Alphabetsonly"
# print(thisstring.isalpha())

# thisstring = "Hi all we are going to use isdigit"  
# print(thisstring.isdigit())   #OUTPUT WILL BE FALSE

# thisstring = "Only Digits 121326"
# print(thisstring.isdigit())     #OUTPUT WILL BE FALSE

# thisstring = "1232354"
# print(thisstring.isdigit())     #OUTPUT WILL BE TRUE

# thisstring = "Hi all we are going to use isalnum"  
# print(thisstring.isalnum())   #OUTPUT WILL BE FALSE


# thisstring = "Hi all we are going to use isalnum121212"  
# print(thisstring.isalnum())   #OUTPUT WILL BE FALSE


# thisstring = "Alphabetsand1213254"  
# print(thisstring.isalnum())   #OUTPUT WILL BE TRUE


# thisstring = "1213254"  
# print(thisstring.isalnum())   #OUTPUT WILL BE TRUE

# thisstring = "profilepicture.jpg"
# print(thisstring.removesuffix(".jpg"))

# thisstring = "profilepicture.jpg"
# print(thisstring.removeprefix("profilepicture"))  #output will be .jpg (removes the given substring)

# thisstring = "onlyalphabets"
# print(thisstring.isalpha())

# messy_string = "!!!Hello World!!!"
# cleaned_string = messy_string.strip("!")
# print(cleaned_string)





# uppercase =  87032845L
# print(uppercase)
# filename = ".txtnotes.txt"
# print(filename.removesuffix(".txt"))
# print(filename.replace(".txt",''))
# print(filename.rstrip(".txt"))
# print(filename.strip(".txnoe"))

# string = "$Hello World$" 
# print(string.lstrip("$"))


# class Animal:
#     def __init__(self,age):
#         self.age = age

# s = Animal(212)
# print(s.age)


class Animal:
    def __init__(self,age):
        self.age = age
        self.kingdom = "Animalia"
    def speak(self):
        print("Animal Speaking")
    def jump(self):
        print("Jumping high")
#The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print(f"dog barking and is from kingdom {self.kingdom}")
#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print(f"Eating bread...and has an age of {self.age}")
    def jump(self):
        print("Jumping lower")   
d = DogChild(22)
d.bark()
d.speak()
d.eat()
d.jump()
