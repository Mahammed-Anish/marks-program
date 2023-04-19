n = int(input("Enter number of subjects : "))
sum = 0
for i in range(n):
	marks = int(input())
	sum += marks
avg = sum/n
if(avg>=90):
	print("0 Grade")
elif(avg>=80 and avg<90):
	print("A Grade")
elif(avg>=70 and avg<80):
	print("B Grade")
elif(avg>=60 and avg<70):
	print("C Grade")
elif(avg>=50 and avg<60):
	print("D Grade")
elif(avg>=40 and avg<50):
	print("Pass")
else:
	print("Fail")
