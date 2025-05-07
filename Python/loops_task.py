'''#Print even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")

#Find and print positive numbers in a list

numbers = [-5, 3, -1, 7, 0, -2, 8]

for num in numbers:
    if num > 0:
        print(f"{num} is positive")

#Count how many times a specific value appears


values = [2, 3, 2, 5, 2, 7, 3]
target = 2
count = 0

for val in values:
    if val == target:
        count += 1

print(f"{target} appears {count} times")

#Task: Sum all positive numbers
numbers = [-3, 5, -1, 9, -8, 4]
total = 0

for num in numbers:
    if num > 0:
        total += num

print("Sum of positive numbers:", total)


#Task: Print numbers NOT divisible by 3

for i in range(1, 21):
    if i % 3 != 0:
        print(i)
#Square of Numbers
for i in range(1, 6):
    square = i ** 2
    print(f"Square of {i} is {square}")'''
    
 for num in range(2, 101):  # start from 2, as 1 is not prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # check up to square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')














