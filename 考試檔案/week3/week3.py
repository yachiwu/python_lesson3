
def priceEq(a,b,c1,c2,n):
	#最初價格
	p1 = []
	p1.append((a+c1)/2)
	p2 = []
	p2.append((a+b*p1[0]+c2)/2)
	for i in range(n):
		p1Next = max((a+b*p2[i]+c1) / 2, 0)
		p1.append(p1Next)
		p2Next = max((a+b*p1Next+c2) / 2, 0)
		p2.append(p2Next)	
	return p1,p2	
def printEq(p1, p2, n):
  for i in range(n + 1):
    s = str(round(p1[i], 2))
    s +=" "+ str(round(p2[i], 2))
    print(s)	

data = input()
a,b,c1,c2,n = data.split(',')
a = float(a)
b = float(b)
c1 = float(c1)
c2 = float(c2)
n = int(n)
p1, p2 = priceEq(a,b,c1,c2,n)

printEq(p1, p2, n)    
p1Eq = p1[n]
p2Eq = p2[n]
print("%0.2f %0.2f" % (p1Eq, p2Eq))

