'''#Creating a Function&Call it
def my_function():
    print("Hello from a function")
my_function()
my_function()


def me():
    print("Name:Manikandan")
    print("Place:Ennakkudi")
    print("Age:21")
me()
'''
'''#Arguments
def my_function(fname):
  print(fname + " Gunasekaran")

my_function("Jothi")
my_function("Manikandan")
my_function("Harikrishnan")

def add(a,b):
  print(a+b)

add(2,5)
'''

#Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Nila", "Deepika", "jothi")

#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Nila", child2 = "Deepika", child3 = "jothi")
