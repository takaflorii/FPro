def local_minima(alist):
    result = []
    for n in range(0, len(alist)-2):    
        neighbour = alist[n:n+3]
        elmnt = min(neighbour)
        if neighbour.count(elmnt) == 1:
            result.append(elmnt)
        else:
            continue
    return result
