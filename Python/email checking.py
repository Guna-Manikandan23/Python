def check():
    a=input("Enter E-mail:")
    s=a.split("@")
    for i in s[1]:
        if('.'in s[1])and(s[1][]):
            print('valid email')
    
check()
