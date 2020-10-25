def isListPalindrome(l):
	slow = l
	stack = []
	ispalin = True

	while slow != None:
		stack.append(slow.value)
		slow = slow.next

	while l != None:
		i = stack.pop()

		if head.value == i:
			ispalin = True
		else:
			ispalin = False
			break
		l = l.next
	return ispalin
# 25/10/20