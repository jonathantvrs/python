from model import MyCPF, MyCNPJ, DocumentFactory, Contact
from validate_docbr import CNPJ

my_cpf = MyCPF("12354367996")
print(my_cpf)

cnpj = CNPJ().generate()
my_cnpj = MyCNPJ(cnpj)
print(my_cnpj)

document = DocumentFactory.create_document("12354367996")
print(document)

telephone = Contact("5584981417758")
print(telephone)


