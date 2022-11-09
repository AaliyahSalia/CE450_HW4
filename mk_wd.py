
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(100)
wd = make_withdraw(100)
print(wd(10))
print(wd(20))
print(wd(100))