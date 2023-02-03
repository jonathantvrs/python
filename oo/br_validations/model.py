import re
from validate_docbr import CPF, CNPJ

class DocumentFactory:
    @staticmethod
    def create_document(document: str):
        if len(document) == 11:
            return MyCPF(document)
        elif len(document) == 14:
            return MyCNPJ(document)
        else:
            raise ValueError("Incorrect document!")

class MyCPF: 
    def __init__(self, cpf: str) -> None:
        if self.__is_valid(cpf):
            self.__cpf = cpf
        else:
            raise ValueError("CPF is not valid!")

    def __str__(self) -> str:
        return self.__cpf_format()

    def __is_valid(self, cpf: str) -> bool:
        cpf_validator = CPF()
        return cpf_validator.validate(cpf)

    def __cpf_format(self) -> str:
        mask = CPF()
        return mask.mask(self.__cpf)

class MyCNPJ:
    def __init__(self, cnpj: str) -> None:
        if self.__is_valid(cnpj):
            self.__cnpj = cnpj
        else:
            raise ValueError("CNPJ is not valid!")

    def __str__(self) -> str:
        return self.__cnpj_format()

    def __is_valid(self, cnpj: str) -> bool:
        cnpj_validator = CNPJ()
        return cnpj_validator.validate(cnpj)

    def __cnpj_format(self):
        mask = CNPJ()
        return mask.mask(self.__cnpj)

class Contact:
    def __init__(self, telephone) -> None:
        if self.__validate(telephone):
            self.__number = telephone
        else:
            raise ValueError("Incorrect number!")

    def __str__(self) -> str:
        return self.__number_format()

    def __validate(self, telephone) -> bool:
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        return re.findall(pattern, telephone)

    def __number_format(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.search(pattern, self.__number)
        return "+{} ({}) {}-{}".format(
            response.group(1),
            response.group(2),
            response.group(3),
            response.group(4)
        )