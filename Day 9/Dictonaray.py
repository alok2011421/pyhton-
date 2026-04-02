programming_dictonaray={
    "Bugs":"An error in the program that prevent it from running as expected",
    "Function":"A piece of code that ypu can call over and over again",
}
#printing a single defination
print(programming_dictonaray["Bugs"]) #Remeber that modt people do type error here

#append in list
programming_dictonaray ["Loop"]= {"A fuction that repeat a function until the condition get false"}

# Editing an dictonaray
programming_dictonaray ["Bugs"]={"A moth in your computer"}

#printing in loop
for words in programming_dictonaray:
    print(words)
    print(programming_dictonaray[words])