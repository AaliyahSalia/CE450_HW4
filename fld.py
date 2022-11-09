from operator import add, sub, mul 

def fld(lst, g, m):
    if not lst:
        return m
    elif(len(lst)) == 1:
        return g(m, lst[0])
    else:
        val = lst[0]
        return g(fld(lst[1:], g, m), val)

s = [3, 2, 1]
print(fld(s, sub, 0))
print(fld(s, add, 0))
print(fld(s, mul, 1))
print(fld([], sub, 100))


        