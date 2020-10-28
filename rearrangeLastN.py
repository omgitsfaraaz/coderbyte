def rearrangeLastN(l, n):
	arrList = []
	while l:
		arrList.append(l.value)
		l = l.next

	arrList = arrList[-n:] + arrList[:-n]
	return arrList