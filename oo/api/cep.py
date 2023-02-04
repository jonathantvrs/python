import requests

class Address:
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.__cep_is_valid(cep):
            self.__cep = cep
        else:
            raise ValueError("CEP is not valid!")

    def __str__(self) -> str:
        return self.__format_cep()

    def __cep_is_valid(self, cep):
        return len(cep) == 8
    
    def __format_cep(self) -> str:
        return "{}-{}".format(self.__cep[:5], self.__cep[5:])

    def get_address(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.__cep)
        response = requests.get(url)
        data = response.json()
        return (
            data['bairro'],
            data['localidade'],
            data['uf']
        )
