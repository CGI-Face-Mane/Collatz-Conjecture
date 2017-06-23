list_c=[]
x=int(input("Starting value" ))
while x>1:
	if x%2==0:
		x=x/2
		list_c.append(x)
	else:
		x=2*x+1
		list_c.append(x)
print(list_c)
print(list_c.len())
