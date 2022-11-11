
def mk_wd(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

withdraw = mk_wd(100)
wd = mk_wd(100)
print(wd(10))
print(wd(20))
print(wd(100))
