def merge_sorted_lists(lst1, lst2):
    alist = lst1 + lst2
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist