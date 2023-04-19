n = int(input("Enter a number to generate fibonacci series: "))
if(n < 0):
    print("Please enter a valid number")
else:
    if(n==0):
        print("0")
    elif(n==1):
        print("0 1")
    else:
        f1 = 0
        f2 = 1
        print(f1,f2,end=" ")
        f3 = f1+f2
        while(f3 <= n):
            print(f3,end=" ")
            f1 = f2
            f2 = f3
            f3 = f1+f2