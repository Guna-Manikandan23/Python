print('Hello')
print("Hello")
print("I'm 'Manikandan' ")
print('I\'m "Deepika"')
print("I'm \"Nila\"")
print('I\'m \'Deepika Manikandan\'')

a='nila'
print(a)
print(a[1])

b="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
print(len(b))

txt="Don't wait for the Oppurtunity,create it!"
print("wait" in txt)
print("love" in txt)
if "dictionary" in txt:
   print("Yes,it is present")
   
else:
    print("No,it is not present")   
    
print("love"not in txt) 
print(txt[2:5])   
print(txt[:10])

n=" I Love Playing Cricket "
print(n.upper())
print(n.lower())
print(n.strip())
print(n.replace("I","J"))
print(n.replace("Playing","to Play"))

d="Hello,Deepika!"
print(d.split(","))

age=21
txt=f"I'm Manikandan and i'm {age}"
print(txt)

cost=100
txt=f"The cost of the bat is {cost:.2f} dollars"
print(txt)

m= "Hello, World"
x=(m[-2:]).upper()
print(x)