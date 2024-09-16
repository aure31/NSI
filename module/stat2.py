
import stats

def medianne(l:list)->float:
    l.sort()
    mid = len(l)//2
    if len(l) % 2 == 0:
        return (l[mid] + l[mid - 1])/2
    return l[mid]