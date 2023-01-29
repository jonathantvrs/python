import re

address = 'Rua Joaquim Eduardo de Farias, 209, Torre E, Ap 102, 59091-130'

cep_pattern = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')

cep_search = cep_pattern.search(address)

if cep_search:
    cep = cep_search.group()
    print(cep)