num = int(input())
ln = len(str(num))
rev = 0
temp = num
while(num !=0):
    rem = num%10
    rev = rev+(rem**ln)
    num //= 10
if(temp == rev):
    print(rev," is Armstrong Number")
else:
    print(rev," is not an Armstrong Number")