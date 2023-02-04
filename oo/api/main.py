import requests
from cep import Address

cep = Address(59091130)

print(cep)

neighbourhood, city, state = cep.get_address()
print(neighbourhood, city, state)