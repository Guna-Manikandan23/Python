'''
a = "apple,orange,banana"
b = a.split(",")

# Replace "orange" with "grapes"
index = b.index("orange")
b[index] = "grapes"

print(b)
'''
print("Welcome to the Python Quiz!")

score = 0  # Initialize score

print("Welcome to the Python Quiz!")

# Question 1
print("\nQuestion 1: What is the output of print(2 ** 3)?")
print("a) 6")
print("b) 8")
print("c) 9")
answer1 = input("Your answer (a/b/c): ")

if answer1 == "b":
    print("Correct!")
    score += 1

    # Question 2
    print("\nQuestion 2: Which of the following is a valid variable name in Python?")
    print("a) 1variable")
    print("b) variable_1")
    print("c) variable-1")
    answer2 = input("Your answer (a/b/c): ")

    if answer2 == "b":
        print("Correct!")
        score += 1

        # Question 3
        print("\nQuestion 3: What is the keyword to define a function in Python?")
        print("a) def")
        print("b) function")
        print("c) fun")
        answer3 = input("Your answer (a/b/c): ")

        if answer3 == "a":
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
    else:
        print("Wrong answer!")
else:
    print("Wrong answer!")

# Final Score
print(f"\nQuiz Over! Your final score is: {score}/3")


#Loan Eligiblity Checker
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score (300-850): "))

if age >= 21:
    if salary >= 3000:
        if credit_score >= 700:
            print("Eligible for premium loan.")
        elif credit_score >= 600:
            print("Eligible for standard loan.")
        else:
            print("Credit score too low for a loan.")
    else:
        print("Salary too low for a loan.")
else:
    print("You must be at least 21 years old to apply.")















