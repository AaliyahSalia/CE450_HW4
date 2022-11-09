def mrg(ls1, ls2):
    sortedList = []
    while (ls1 and ls2):
        if (ls1[0] <= ls2[0]): 
            item = ls1.pop(0) 
            sortedList.append(item)
        else:
            item = ls2.pop(0)
            sortedList.append(item)


    sortedList.extend(ls1 if ls1 else ls2)

    return sortedList

print(mrg([1, 3, 5],[2, 4, 6]))
print(mrg([], [2, 4, 6]))
print(mrg([1, 2, 3], []))
print(mrg([5, 7], [2, 4, 6]))


   