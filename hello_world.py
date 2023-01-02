#print("hello world")
# comments
''' multi line comments



FName, Mname, Lname = input("add in your full name").split(" ",3)
'''
def recieve_Dict(**DicT):
    for keys, Values in DicT:
        print(keys,Values)
    return DicT
def printer(**DicT):
    for values in DicT.items:
        print(values)
def Change_tuple (*x):
    for values in x:
        print(values)
    return x    
def Change_List(*List_):
    list(List_)
    print(List_)
