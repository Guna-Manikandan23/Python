'''a=3
print(a+3)
print(a-3)
print(a*3)
print(a//3)
print(a%3)
a+=5
print(a)

a-=2
print(a)

a*=2
print(a)

print(a>10 and a<20)
print(not(a>10 and a<20))   

b=10
c=5
if c<b: 
   print("B is greater than C")

elif c>b:
   print("C is greater than B")

m=10
d=15
if m<d:print(m)

print(d) if m<d else print(m)

num1=43
if num1>30:
   print("above 30",end="")
   if num1>40:
      print(" and also above 40")
   else:
      print("and not greater than 40")


mdn="Manikandan"
print(f"Name of the person is:{mdn}")'''
a=int(input(""))
if(a%4==0 and a%100!=0)or(a%100==0):
    print("Leap Year")
else:
    print("Non-Leap Year")















   
