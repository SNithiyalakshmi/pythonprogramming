 def getl():
	l=[]
	r=[]
	while(True):
		try:
			c,d= map(int,sys.stdin.readline().split())
		except ValueError:
			break
		l.append(c)
		l.append(d)
		r.append(l)
		l=[]
	for i in r:
		print(i[1]-i[0])
try:
	getl()
except:
	print('invalid')
