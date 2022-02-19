def removeKFromList(l, k):
	current = l
	prev = None

	while current != None:
		if current.value == k:
			if prev == None:
				l = current.next
				current = l
			else:
				prev.next = current.next
				current = current.next
		else:
			prev = current
			current = current.next

# 25/10/20