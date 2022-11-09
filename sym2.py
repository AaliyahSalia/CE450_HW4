def sym(l):
    half = int(len(l) / 2)

    if len(l) % 2 == 0:
        first_str = l[:half]
        second_str = l[half:]
    else:
        first_str = l[:half]
        second_str = l[half+1:]

    if first_str == second_str:
        return True
    return False

print(sym([]))
print(sym([1]))
print(sym([1, 4, 5, 1]))
print(sym([1, 4, 4, 1]))
print(sym(['l', 'o', 'l']))
    