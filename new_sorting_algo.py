import math

l = [6, 76, 1,-444,10201, 0, -34]
sl = []

infinite = math.inf
def min_sort(lst):
    ind = 0
    if lst.count(infinite) == len(lst):
        return sl

    mn = min(lst)
    ind = lst.index(mn)
    lst[ind] = infinite
    sl.append(mn)

    return min_sort(lst)


print(min_sort(l))
