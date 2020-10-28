def reverseNodesInKGroups(l, k):
	curr = l
	mainList = []

	while curr:
		checkcurr = curr
		tempList = []
		tempTrack = 0

		while checkcurr:
			tempTrack += 1
			checkcurr = checkcurr.next
			if tempTrack == k:
				break

		if tempTrack == k:
			for i in range(tempTrack):
				tempList.append(curr.value)
				curr = curr.next
			tempList.reverse()
			mainList.extend(tempList)
		else:
			for i in range(tempList):
				tempList.append(curr.value)
				curr = curr.next
			mainList.extend(tempList)
			
	return tempList