# For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
# swapLexOrder(str, pairs) = "dbca".

# By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".

def swapLexOrder(string, pairs):
    elems = list(string)
    connected = []
    for pair in pairs:
        current_con_ind = -1
        to_delete_ind = []
        for j in range(len(connected)):
            if pair[0] in connected[j] or pair[1] in connected[j]:
                if current_con_ind == -1:
                    connected[j].extend(pair)
                    connected[j] = sorted(list(set(connected[j])))
                    current_con_ind = j
                else:
                    connected[current_con_ind].extend(connected[j])
                    to_delete_ind.append(j)
                    connected[current_con_ind].extend(pair)
                    connected[current_con_ind] = sorted(list(set(connected[current_con_ind])))

        for d in to_delete_ind:
        	del connected[d]

        if current_con_ind == -1:
            connected.append(sorted(pair))
    print(connected)

    for indeces in connected:
        substring = []
        for index in indeces:
            substring.append(string[index-1])
        substring = sorted(substring, reverse=True)
        for i in range(len(indeces)):
            elems[indeces[i]-1] = substring[i]
    return ''.join(elems)
