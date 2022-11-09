def rm_all(elem, lst):
    try:
        while True:
            lst.remove(elem)
    except ValueError:
        pass
 
    print(lst)  

elem = int(input("Please enter the element you want to remove: "))
x = [3, 1, 2, 1, 5, 1, 1, 7]
rm_all(elem, x)