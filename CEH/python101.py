#!/bin/python3
#function for a new line 

def new_line():
    print("\n")
#print string 
print ("String and things: ")
print ('Hello world')
print("""Hello this is a 
multiline string""")
print("This is a "+"concatenated string")

print ("\n") #this is a new line 
#Math
print ("Math time: ")
print(50 + 50)#add
print(50 - 50)#subtract
print(50 * 50)#mulitply
print(50  / 50)#divide
print (50+50*50/50)
print (50**2)#exponent
print (50%6) #modulus
print (50 // 6) #number without leftovers

print ("\n")
#variables and methods
print("Variables and methods: ")

quote="All is fair in love and war"
print(quote)
print(len(quote))#prints the length of the quote
print(quote.upper())#turns to uppercase
print(quote.lower())# turns to lower case
print(quote.title())# to title form ,capitalizes every first letter

name="Heath"
age=29 #int(29)
gpa=3.7 #float(3.7)
print(age)
print(int(29.9))#does not round off
print ("My name is "+name +" and I am " +str(age) + " years old")

print ("\n")
age+=1
print(age)

birthday=1
age+=birthday
print(age)

print ("\n")
print("Functions :")
def who_am_I():
    name="Heath"
    age=29
    print ("My name is "+name +" and I am " +str(age) + " years old")
who_am_I()

#adding parameters
def add_one_hundred(num):
    print(num+100)
add_one_hundred(50)
#adding multiple parameters
def add(x,y):
    print(x+y)
add(56,44)
#using return
def multipy(a,b):
    return a*b
print(multipy(5,7))

#finding the square root
def square_root(num):
    return num ** .5
print(square_root(49))


new_line()
print("Boolean expressions: ")
bool1=True
bool2=3*3==9
bool3= False
bool4= 3*3 !=9
print(bool1, bool2, bool3, bool4)
print(type(bool1))
bool5="True"
print(type(bool5))

#relational and boolean operators
greater_than= 7>5
lesser_than =5<7
greater_than_equal_to= 7>=5
lesser_than_equal_to =5<=7
print(greater_than,lesser_than,greater_than_equal_to,lesser_than_equal_to)

test_and= (7>5) and (5<7)
test_or= (7>5) or (5<7)
test_not= not True
print(test_and,test_not, test_or)

new_line()
print("Conditional statements: ")
def soda(money):
    if money >=65:
        return "You've got yourself a soda !"
    else:
        return "No soda for you !"
print(soda(80))
print(soda(55))

def alcohol(money, age):
    if (money>=65) and (age>=18):
        return "We're getting tipsy"
    elif (money <=64) and (age>=18):
        return "You are broke!! You need more cash !!"
    elif (age<=17) and (money>=65):
        return "Sorry, You are still under age to drink alcohol"
    else:
        return "No soda for you !!!"
print(alcohol(85,21))
print(alcohol(76,13))
print(alcohol(45,33))
print(alcohol(13,10))

new_line()
print("Lists have brackets : ")
movies=["When Harry met Sally", "The Hangover","The Perks of being a WallFlower", "The Exorcist"]
print(movies[0]) #call the first movie in the list
print(movies[0:2])#first and second item in the list
print(movies[-1])#last item in the list
print(len(movies)) #how many items are there in the list

movies.append("Jaws of Death")#add item to the list
print (movies)
print(len(movies))
movies.pop()# removes the last item to the list
print(movies)
movies.pop(1)# remove a specifiv item in the list
print(movies)
movies=["When Harry met Sally", "The Hangover","The Perks of being a WallFlower", "The Exorcist"]
person=["Heath","Jake", "Leah", "Jeff"]
combined= zip(movies,person)
print(list(combined))

new_line()
#tuples are static, they do not change
print("Tuples have paranthesis and cannot change, they are immutable:  ")
grades=("A","B","C","D","E")
print(grades)
print(grades[1])

new_line()
#Loops
print("For loops : start to finish for iterate")
vegetables=["Cucumber", "Spinach","Cabbage"]
for x in vegetables:
    print(x)

new_line()
print("while loops- execute as long as it is true: ")
i=1
while i<10:
    print(i) 
    i +=1
 