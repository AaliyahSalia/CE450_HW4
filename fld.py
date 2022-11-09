from operator import add, sub, mul

def fld(lst, g, m):
    if lst == []:
        return m
    else:
        return g(fld(lst[1:], g, m), lst[0])

print(fld([3, 2, 1], sub, 0))
print(fld([3, 2, 1], add, 0))
print(fld([3, 2, 1], mul, 1))
print(fld([], sub, 100))
