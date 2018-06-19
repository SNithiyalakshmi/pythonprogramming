a=int(raw_input())
sum=0
k=a
while(a!=0):

	a=a%10
	sum=sum*10+b
	a=a/10
if(sum==k):
	print("palindrome")
else:
	print("not palindrome")
