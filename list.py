#create list
l =["apple", "banana", "mango","kiwi"]
print(l[1])
#negative index
#-1 refers to the last item
print(l[-1])
#range of index
#in list indexing start from 0
print(l[1:3])
#Check if Item Exists
if 'apple' in l:
    print("apple is in the list")
else:
    print("apple is not in the list")
#change the value of a list item
l[1]="watermelon"
print(l)
#Change a Range of Item Values
#Remember that the first item is position 0,
#and note that the item in last position of the range is NOT included
print(l[1:3])
l[1:3]=["banana","grapes"]
print(l)
#to add items in the list
#use append() to add any item at the end of the list
l.append("papaya")
print(l)
#to add at the specific index use insert function
l.insert(2,"orange")
print(l)
#to remove the item use remove method
l.remove("orange")
print(l)
#to remove specified index item use pop() or del method
l.pop(2)
print(l)
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
#syntax: newlist=[expression for item in iterable if condition]

