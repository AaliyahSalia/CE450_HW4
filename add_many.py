def add_many(x, elem, lst):
    for i in range(x):
        lst.append(elem)

lst = [1, 2, 4, 2, 1]
print(lst)
add_many(2, 5, lst)
print(lst)

