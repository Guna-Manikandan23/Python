#Amstrong Number
num = int(input("Enter a 3-digit number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10
'''
if sum == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")

# Keep asking for a password until it's correct
password = ""
while password != "secret123":
    password = input("Enter the password: ")
print("Access granted!")

# Sum numbers until the user types 0
total = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))
print("Total sum is:", total)
#Countdown from 5 to 1
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Blast off!")


# Print only even numbers between 1 and 20

num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1


#Simple login system (3 tries only)
correct_username = "admin"
correct_password = "1234"
tries = 0

while tries < 3:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect. Try again.")
        tries += 1

if tries == 3:
    print("Too many attempts. Access denied.")


#Simulate a basic calculator (until user exits)
while True:
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Unknown operator")

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != "yes":
        break

#Create a multiplication table for a given number

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
    
#Palindrome Number-
num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

if original == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")

#find the given string is palindrome or not
text = input("Enter a string: ")
left = 0
right = len(text) - 1
is_palindrome = True
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#Adam Number
num = int(input("Enter a number: "))
reverse_num = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp = temp // 10
square_original = num * num
square_reversed = reverse_num * reverse_num
reverse_square_reversed = 0
temp = square_reversed
while temp > 0:
    digit = temp % 10
    reverse_square_reversed = reverse_square_reversed * 10 + digit
    temp = temp // 10

# Check if Adam number
# Input number
num = int(input("Enter a number: "))

# Reverse the original number
reverse_num = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp = temp // 10

# Square the original number
square_original = num * num

# Square the reversed number
square_reversed = reverse_num * reverse_num

# Reverse the square of reversed number
reverse_square_reversed = 0
temp = square_reversed
while temp > 0:
    digit = temp % 10
    reverse_square_reversed = reverse_square_reversed * 10 + digit
    temp = temp // 10

# Check if Adam number
if square_original == reverse_square_reversed:
    print("Adam Number")
else:
    print("Not an Adam Number")'''

















