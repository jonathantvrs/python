# tuples are comma-separated values
account = 'jonathan', 24
print(account) # print ('jonathan', 20)

# explicit assignment
account = ('rebeka', 25)
print(account)

# tuples are indexable and immutable 
print(account[0], account[1])
# account[0] = 'johnny' # TypeError

# its possible to create tuples of tuples
account1 = 'jonathan', 24
account2 = 'rebeka', 25
accounts = account1, account2
print(accounts) # print (('jonathan', 24), ('rebeka', 25))
account3 = 'johnny', 57
accounts = accounts, account3
print(accounts) # print ((('jonathan', 24), ('rebeka', 25)), ('johnny', 57))

# list of tuples
accounts = []
accounts.append(account1)
print(accounts) # print [('jonathan', 24)]
accounts.append(account2)
accounts.append(account3)
print(accounts) # print [('jonathan', 24), ('rebeka', 25), ('johnny', 57)]