def  f(suits, numbers):
    list = []
    for suit in suits:
        for num in numbers:
            list.append((suit, num))
    return list

print(f(["S", "C"], [1,2,3]))
print(f(["S", "C"], [3,2,1]))
print(f([], [3,2,1]))
print(f(["S", "C"], []))