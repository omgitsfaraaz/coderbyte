def mergeTwoLinkedLists(l1, l2):
	newList = []
	currone = l1
	currtwo = l2

	while currone or currtwo:
		if currone:
			pass
		else:
			while currtwo:
				newList.append(currtwo.value)
				currtwo = currtwo.next
			break

		if currtwo:
			pass
		else:
			while currone:
				newList.append(currone.value)
				currone = currone.next
			break

		if currone.value < currtwo.value:
			newList.append(currone.value)
			currone = currone.next
		elif currone.value == currtwo.value:
			newList.append(currone.value)
			newList.append(currtwo.value)
			currone = currone.next
			currtwo = currtwo.next
		else:
			newList.append(currtwo.value)
			currtwo = currtwo.next

	return newList