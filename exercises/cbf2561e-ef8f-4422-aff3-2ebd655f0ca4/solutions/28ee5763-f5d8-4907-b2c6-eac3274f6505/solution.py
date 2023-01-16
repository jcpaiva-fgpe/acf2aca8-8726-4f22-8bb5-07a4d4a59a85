def harshad(n):
	array = []

	for i in range(1,n+1):
		h = i
		s = 0
		while i >0:
			s += i%10
			i = i//10

		if (h%s == 0):
			array.append(h)

	return array