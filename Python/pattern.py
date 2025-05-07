#right-angled triangle pattern
rows = 5
for i in range(1, rows + 1):
    print('*' * i)
#right-angled triangle pattern aligned to the right
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)

n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")
    print() 


""" n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  """




- 1))
 """
""" n = 5
for i in range(1, n + 1):
    print(" ".join(str(i) for x in range(i))) """

''' 
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
''' 

""" n = 5
for i in range(n, 0, -1):
    print("*" * i)


n = 5
for i in range(1, n + 1):
    print("*" * i)
"""    
'''
# int pattern
n = 5
for i in range(1, n+1):
    print(" " * (n - i) +str(i)* (2 * i - 1))
'''
