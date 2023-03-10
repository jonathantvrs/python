from functools import total_ordering

@total_ordering
class Account:
    
    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def __eq__(self, other):
        return self.__number == other.__number

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __str__(self):
        return f'Balance: {self.__balance}'

    def get_statement(self):
        print("Owner: {}".format(self.__owner))
        print("Balance: {}".format(self.__balance))
        print("Limit: {}".format(self.__limit))

    def deposit(self, amount):
        if (amount > 0):
            self.__balance += amount

    def __has_limit(self, withdrawal_amount):
        available_amount = self.__balance + self.__limit
        return withdrawal_amount <= available_amount

    def withdraw(self, amount):
        if (self.__has_limit(amount)):
            if (self.__balance >= amount):
                self.__balance -= amount
            else: 
                if (self.__balance > 0):
                    amount -= self.__balance
                    self.__balance = 0
                
                self.__limit -= amount 

    def transfer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)

    @property
    def owner(self):
        return self.__owner
    
    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

account1 = Account(10, 'Jonathan', 1.0, 10.0)
account2 = Account(10, 'Jonathan', 10.0, 10.0)
account3 = Account(10, 'Jonathan', 10.0, 10.0)


print(account1 == account2) # print True
print(account1 < account2) # print True

accounts = [account1, account2]
for account in sorted(accounts, reverse=True):
    print(account)

print(account2 <= account3) # print True 