n=int(input("How many elements??"))
c=[]
for x in range(n):
	k=int(input())
	c.append(k)
b=sorted(a)
if c==b:
	print("Yes")
else:
	print("No")
