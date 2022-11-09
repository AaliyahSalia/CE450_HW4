def fltn(ls):
    if ls == []:
        return ls

    if isinstance(ls[0], list):
        return fltn(ls[0]) + fltn(ls[1:])

    return ls[:1] + fltn(ls[1:])

x = [1, 2, 3]
print(x)
print(fltn(x))
x = [1, [2, 3], 4]
print(fltn(x))
x = [[1, [1, 1]], 1, [1, 1]]
print(fltn(x))

