import random


mylist = [] #create a list
for i in range(100):
    randint = random.randint(0,100) #gemerate random number
    mylist.append(randint)  #add random number into the list

mylistlen = len(mylist) #length of our list
# print(mylistlen) #check length of list = 100
# print(mylist)

def sortlist(list): #create a function that sorts list
    sortedlist = [] #create a list without elements
    while len(mylist) != 0: #while there is an element in mylist:
        for element in mylist: #for each elemenet
           if element == min(mylist): #if element is minimum value, 
                sortedlist.append(element) #add the element into the sortedlist
                mylist.remove(element) #remove the element from mylist
    return sortedlist

sortedlist = sortlist(mylist) 
# print(sortedlist)

def averageofevennumbers(list): #function to return average of evennumbers 
    counter = 0 #create a counter variable 
    sum = 0 #create a sum variable
    for element in list: #for every lement in list
        if element % 2 == 0: #if element is even:
            counter += 1 #add +1 to counter 
            sum += element #add element to sum variable 
    return sum / counter #divide sum by counter

print( averageofevennumbers(sortedlist) ) 

def averageofoddnumbers(list): #function to return average of odd numbers 
    counter = 0 #create a counter variable
    sum = 0 #create a sum variable
    for element in list: #for every element in list 
        if element % 2 != 0: #check if element is odd
            counter += 1 #add +1 to counter 
            sum += element #add element to sum variable 
    return sum / counter #divide sum by counter 

print( averageofoddnumbers(sortedlist) )


