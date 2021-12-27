
def factorial(n):
	s=1
	if n<0:
		return -1
	elif n==0:
		return 1
	else:
		for i in range(n):
			s=s*i
		return s
		

print("input should be an integer")
n=int(input())
print(facorial(n))
