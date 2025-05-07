'''#Print numbers 1 to 10
for i in range(1, 11):
    print(i)

#Print even numbers between 1 and 20

for i in range(2, 21, 2):
    print(i)

#Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i

print("Sum is:", total)
   
n = 100
total = n * (n + 1) // 2
print("Sum is:", total)

#Print each character in a string

text = "Hello, world!"

for char in text:
    print(char)
#vowels in a string
text = "Python is Awesome!"
vowels = 'aeiouAEIOU'
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#Reverse a string using a for loop
text = "hello"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text  # Add each char to the front

print("Reversed string:", reversed_text)

#Find the factorial of a number'''



a=123
str_a=str(a)
rev_num=""
for i in str_a:
    rev_num=i+rev_num
print(rev_num)   

#Fibonacci series
a=0
b=1
for i in range(10):
    print(a)
    c=a+b
    a=b
    b=c
a=0
b=1
count=0
#Amstrong Number
num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
total = 0

for digit in num_str:
    total += int(digit) ** num_digits

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")




























   
