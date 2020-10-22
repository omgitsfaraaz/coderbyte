a = [2, 1, 3, 5, 3, 2]


def firstDuplicate(a):
	seen = set()

	for i in a:
		if i in seen:
			return i
		seen.add(i)
	return -1

firstDuplicate(a)