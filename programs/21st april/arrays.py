from array import *
a = array.array('i',[1,2,3,4])
print(type(a))


n = int(input())
for i in range(n):
    for k in range(n-i-1):
        print(" ")
    for j in range(2*i-1):
        print("* ")
    print()
