def printv(val,n):
	for a in range(n):
		print(val)

def main():
	try :
		value=input()
		n=int(input())
		printv(value,n)
	except:
		print('invalid input')
main()
