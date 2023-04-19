num = int(input())
rev = 0
temp = num
while(num !=0):
    rem = num%10
    rev = (rev*10)+rem
    num //= 10
if(temp == rev):
    print(num," is palindrome")
else:
    print(num," is not a palindrome")