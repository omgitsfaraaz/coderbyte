def firstNotRepeatingCharacter(s):
	a = {}
	b = []

	for i in s:
		if i in a:
			a[i] += 1
		else:
			a[i] = 1
			b.append(i)

	for i in b:
		if a[i] == 1:
			return i
	return '_'