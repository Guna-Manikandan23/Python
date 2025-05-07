'''
sample=" hello python world"
a=len(sample)

words=sample.strip().split(" ")
print(words[int(len(words)/2)])

name="greeting to all"
b=len(sample)

words=name.strip().split(" ")
print(words[int(len(words)/2)])


name=input("enter your name")
print(name)
a=len(name)
print(name[int (a/2)])


name='Manikandan' import logging

logging.basicConfig(level=logging.INFO)

sample=" hello python world"

logging.info(f"Sample string: {sample}")
a=len(sample)
logging.info(f"Length of sample string: {a}")

words=sample.strip().split(" ")
logging.info(f"Words in sample string: {words}")
print(words[int(len(words)/2)])

name="greeting to all"
b=len(sample)
logging.info(f"Length of sample string (again): {b}")

words=name.strip().split(" ")
logging.info(f"Words in name string: {words}")
print(words[int(len(words)/2)])

name=input("enter your name")
logging.info(f"User input: {name}")
print(name)
a=len(name)
logging.info(f"Length of user input: {a}")
print(name[int (a/2)])

name='Manikandan'
logging.info(f"Name: {name}")
print(name)
print("length:",len(name))
logging.info(f"Length of name: {len(name)}")
print("uppercase:",name.upper())
logging.info(f"Uppercase name: {name.upper()}")
print("lowercase:",name.lower())
logging.info(f"Lowercase name: {name.lower()}")
print("titlecase:",name.title())
logging.info(f"Titlecase name: {name.title()}")
print("capitalize:",name.capitalize())
logging.info(f"Capitalized name: {name.capitalize()}")
print("swapcase:",name.swapcase())
logging.info(f"Swapcase name: {name.swapcase()}")

print("isupper:","NAME".isupper())
logging.info(f"Is 'NAME' uppercase: {'NAME'.isupper()}")
print("islower:","name".islower())
logging.info(f"Is 'name' lowercase: {'name'.islower()}")
print("isalpha:","name".isalpha())
logging.info(f"Is 'name' alphabetic: {'name'.isalpha()}")
print("isdigit:","1234".isdigit())
logging.info(f"Is '1234' digit: {'1234'.isdigit()}")
print("isalphanumeric:","name 123".isalnum())
logging.info(f"Is 'name 123' alphanumeric: {'name 123'.isalnum()}")

school=input("enter your school")
logging.info(f"User input: {school}")
print(school)
print("length:",len(school))
logging.info(f"Length of school: {len(school)}")
print("uppercase:",school.upper())
logging.info(f"Uppercase school: {school.upper()}")
print("lowercase:",school.lower())
logging.info(f"Lowercase school: {school.lower()}")
print("titlecase:",school.title())
logging.info(f"Titlecase school: {school.title()}")
print("capitalize:",school.capitalize())
logging.info(f"Capitalized school: {school.capitalize()}")
print("swapcase:",school.swapcase())
logging.info(f"Swapcase school: {school.swapcase()}")

print("isupper:","SCHOOL".isupper())
logging.info(f"Is 'SCHOOL' uppercase: {'SCHOOL'.isupper()}")
print("islower:","school".islower())
logging.info(f"Is 'school' lowercase: {'school'.islower()}")
print("isalpha",school.isalpha())
logging.info(f"Is school alphabetic: {school.isalpha()}")
print("isdigit:","1234".isdigit())
logging.info(f"Is '1234' digit: {'1234'.isdigit()}")
print("isalphanumeric:","school 123".isalnum())
logging.info(f"Is 'school 123' alphanumeric: {'school 123'.isalnum()}")
print(name)
print("length:",len(name))
print("uppercase:",name.upper())
print("lowercase:",name.lower())
print("titlecase:",name.title())
print("capitalize:",name.capitalize())
print("swapcase:",name.swapcase())


print("isupper:","NAME".isupper())
print("islower:","name".islower())
print("isalpha:","name".isalpha())
print("isdigit:","1234".isdigit())
print("isalphanumeric:","name 123".isalnum())

school=input("enter your school")
print(school)
print("length:",len(school))
print("uppercase:",school.upper())
print("lowercase:",school.lower())
print("titlecase:",school.title())
print("capitalize:",school.capitalize())
print("swapcase:",school.swapcase())

print("isupper:","SCHOOL".isupper())
print("islower:","school".islower())
print("isalpha",school.isalpha())
print("isdigit:","1234".isdigit())
print("isalphanumeric:","school 123".isalnum())

'''

sample =" Hello, Python World!  "
words = sample.strip().split("o")  # Splits into list
print("Split into Words:", words)
print("Join with '-':", "-".join(words))  # Joins list into string

# Find, Replace, Count
print("Index of 'Python':", sample.find("Python"))  # Returns first index
print("Replace 'Python' with 'Java':", sample.replace("Python", "Java"))
print("Count of 'o':", sample.count("o"))























    

