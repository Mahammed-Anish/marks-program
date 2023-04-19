a = int(input())
b = int(input())
c = int(input())

if(a==b):
    if(a>c):
        temp = c
        c = a
        a = temp
elif(b==c):
    if(b>a):
        temp = b
        b = a
        a = temp
elif(a==c):
    if(c>b):
        temp = c
        c = b
        b = temp
else:
    if(a>b and a>c):
        if(b>c):
            temp = a
            a = c
            c = temp
        else:
            temp = c
            c = b
            b = temp
    elif(b>a and b>c):
        temp = c
        c = b
        b = temp
        if(a>b):
            temp = a
            a = b
            b = temp
    else:
        if(a>b):
            temp = b
            b = a
            a = temp
print(a,b,c)
