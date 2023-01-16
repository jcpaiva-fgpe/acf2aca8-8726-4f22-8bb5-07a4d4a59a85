def harshad(n):
	s = 0
	h = n
	
	while n > 0:
		s += n%10
		n = n //10
	if(h%s == 0):
		return 'YES'
	else:
		return 'NO'
