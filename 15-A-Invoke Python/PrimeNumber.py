def PrimeNumber(n):
	n=int(n)
	if n<=1:
		return False
	if n==2:
		return True
	for i in range(2,n//2):
		if n%i==0:
			return False
	return True
