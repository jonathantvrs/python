from decimal import Decimal

earnings = 42.99 * 5
expenses = 49.2 * 3

print(earnings) # 214.95000000000002
print(expenses) # 147.60000000000002

earnings = Decimal('42.99') * 5
expenses = Decimal('49.2') * 3

print(earnings) # 214.95 
print(expenses) # 147.6
