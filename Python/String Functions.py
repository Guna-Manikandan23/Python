sample =" Hello, Python World!  "

#print("Original String:", sample)


# Basic String Operations
print("Length:", len(sample))
print("Upper Case:", sample.upper())
print("Lower Case:", sample.lower())
print("Title Case:", sample.title())
print("Capitalize:", sample.capitalize())
print("Swap Case:", sample.swapcase())

# Strip, LStrip, RStrip
print("Stripped:", sample.strip())  # Removes leading & trailing spaces
print("Left Stripped:", sample.lstrip())  # Removes left spaces
print("Right Stripped:", sample.rstrip())  # Removes right spaces

# String Checking Functions
print("Starts with 'Hello':", sample.strip().startswith("Hello"))
print("Ends with 'World!':", sample.strip().endswith("World!"))
print("Is Alpha:", "Python".isalpha())  # Checks if all chars are alphabets
print("Is Digit:", "1234".isdigit())  # Checks if all chars are digits
print("Is Alphanumeric:", "Python123".isalnum())  # Checks if alpha + num
print("Is Lower:", "python".islower())  # Checks if all are lowercase
print("Is Upper:", "PYTHON".isupper())  # Checks if all are uppercase


# Find, Replace, Count
print("Index of 'Python':", sample.find("Python"))  # Returns first index
print("Replace 'Python' with 'Java':", sample.replace("Python", "Java"))
print("Count of 'o':", sample.count("o"))



# Split and Join
words = sample.strip().split("o")  # Splits into list
print("Split into Words:", words)
print("Join with '-':", "-".join(words))  # Joins list into string


# Formatting Strings
name, age = "Alice", 25
print("Formatted String:", f"My name is {name} and I am {age} years old.")
    
# Encoding and Decoding
encoded = sample.encode("utf-8")
print("Encoded String:", encoded)
print("Decoded String:", encoded.decode())
print("Reversed String:", sample[::-1])
    
a="hello"
print(a[0])
print(a[1:4])
print(a[-3:-1])
print(a[:4])
print(a[2:])
print(a[::3])
print(a[::-2])
