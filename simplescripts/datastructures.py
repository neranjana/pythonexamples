mylist=[2001, 2002, 2003, 2002]
# lists can contain dupulicates
print("the entire mylist")
print(mylist) # prints the entire list
print("the element in index 2 of mylist")
print(mylist[2]) # prints the element in index 2
mylist.append(2006) # appends to the list
print("appended list")
print(mylist)
mylist[2]=2013 # updates element at index 2 of my list
print("updated mylist")
print(mylist)

mytuple=(3001, 3002, 3003, 3002)
# tuple can contain dupulicates but is imutable
print("the entire tuple")
print(mytuple) # prints the entire tuple
print("the element in index 2 of my tuple")
print(mytuple[2]) # prints the element in index 2

myset={4001, 4002, 4003} # sets cannot contain duplicates
print("entire myset")
print(myset)
print("element at index 1 of myset")
# print(myset[1]) does not work becuase sets don't have an order

numbers=[4000, 4001, 4002, 4001] # a list
print("type of numbers is")
print(type(numbers))
numbers=set(numbers) # converts to a set and remuves duplicates
print("type of numbers now is")
print(type(numbers))
numbers=list(numbers) # converts back to a list
print("type of numbers now is")
print(type(numbers))

mydictionary={"firstyear":2001, "secondyear": 2002, "thirdyear": 2003} # a dicgionary
print("the entire dictionary")
print(mydictionary)
print("value of element with key secondyar")
print (mydictionary["secondyear"])

anotherlist=list(range(2000, 2020, 2)) # create a list from 2000 to 2020 (excluding 2020) step 2
print("LIst from 2000 to 2020 with a step of 2")
print(anotherlist)

firstslice=anotherlist[2:6] #list containing the index 2 to index 6, excluding index 6
print(firstslice)
secondslice=anotherlist[:6] # list containing upto index 6 from begining
print(secondslice)
thirdslice=anotherlist[6:] # list containing elements from index 6 to the last inderx
print(thirdslice)
fourthslice=anotherlist[-4:] # list containing elements from index -4 from end to the last inderx
print(fourthslice)

myString="Neranjana"
print(myString[4]) # prints charachter on the index 4
print(myString[2:5]) # prints characters from index 2 to 5, excluding five

# iterating throuth a list
print("terating though a list")
for item in anotherlist:
    print(item)

# similarly
print("iterating through range starting at 20 ending at 32 step 4")
for item in range(20, 32, 4):
    print(item)


