def chk_elm(lst, n):
    for item in lst:
        if isinstance(item, list):
            if chk_elm(item, n):
                return True
        else:
            if item == n:
                return True
    return False

a = [ [1,[2]], 3, [ [4], [5,[6] ] ]   ] 
print(chk_elm(a, 6))
print(chk_elm(a, 9))