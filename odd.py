n=input()
s=n.split()
a=int(s[0])
b=int(s[1])
for i in range(a+1,b):
	if i%2!=0:
		print(i)

