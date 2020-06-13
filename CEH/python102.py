#!/bin/python3
def new_line():
    print("\n")
print("Importing modules :")

import sys #system functions and parameters
from datetime import datetime
print(datetime.now())

#setting a module as an alias name
from datetime import datetime as dt #using an alias
print (dt.now())

new_line()
#Advanced strings
print("Adnvanced strings: ")
my_name="Heath"
print(my_name[0])# grab first initial of the name
print(my_name[-1]) #grab last initial of the name
sentence="This is a sentence."
print(sentence[:4]) #first word
print(sentence[-9:-1]) #the -1 removes the period at the end
print(sentence.split())
sentence_split=sentence.split()
sentence_join=" ".join(sentence_split) #joing back the sentence with blank space as the delimitor
print(sentence_join)
print("\n".join(sentence_split))

quoteception="I said, 'Give me all the money.'"
print(quoteception)
quoteception="I said, \"Give me all the money.\""
print(quoteception)

print("A" in "Apple")
letter="A"
word="apple"
answer=letter.lower() in word.lower() #improved- case insenstitve
print(answer)

too_much_space="             Hello        "
print(too_much_space.strip()) #removes the blank spaces

full_names="eath Adams"
print(full_names.replace("eath", "Heath"))

movie="The Hangover"
print("My favorite movies is {}".format(movie))#this will fill the blank space


def favorite_book(title,author):
    fav="My favorite book is \" {}\", which is written by {}".format(title, author)
    return fav
print(favorite_book("When the sun goes down","Paul Coelho"))

new_line()

#Dictionaries
print("Dictionaried are keys and values :")
drinks={
    "White Russians": 7,
    "Old Fashions": 10,
    "Lemon Drop":8,
    "Buttery Nipple":6
}
#drink is key and price is value
print(drinks)

employees={
    "Finance":["Bob","Linda", "Tina"],
    "IT":["Gene", "Louise", "Teddy"],
    "HR":["Jimmy Jr","Mort",""]
}
print(employees)
employees["Legal"]=["Mr. Fond"] #add new key: value pair 