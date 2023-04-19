num = int(input())
rev = 0
temp = num
while(num !=0):
    rem = num%10
    rev = rev+(rem*rem*rem)
    num //= 10
if(temp == rev):
    print(rev," is Armstrong Number")
else:
    print(rev," is not an Armstrong Number")