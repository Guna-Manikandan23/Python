#simple for
for x in range(15):
    print("run this time",x)











#for and break
for x in range(8):
        if x==5:
            continue
        print(x)

''' 
#for else
for x in range(12):
    print(x)
    if x==18:
        break
else:
    print("loop ended")

'''


#for and continue
for x in range(8):
        if x==5:
            continue
        print(x)
        
#for using string


string="good day"
for x in string:
    print(x)


#collection in for loop
collection=['hii',2,'well']
for x in collection:
    print(x)

#nested in for loop
color=["red","sweet","tasty"]
fruits=["cherry","plums","apple"]
value=["x","y","z"]
for a in color:
    for b in fruits:
        for c in value:
            print(a,b,c) 






 
#list in for loop
lists=[["a","b","c"],["d","e","f"],["g","h","i"]]
for l in lists:
    print(l)
    for x in l:
        print(x)


#continue statement
fruits=["apple","cherry","banana","grapes"]
for x in fruits:
    if x=="banana":
      continue
    print(x) 


#increase value
for x in range(3,45,6):
    print(x) 

'''
