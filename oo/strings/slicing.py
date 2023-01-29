fullname = 'Jonathan Tavares da Silva'
# print full name
print(fullname)
# print a substring of the fullname 0-8 
# (the last number is not inclusive)
firstname = fullname[0:8]
print(firstname)
# print a substring of the fullname 9-16
midname = fullname[9:16]
print (midname)


# using find method
url = 'https://alura.com.br/busca?query=python'

question_mark_index = url.find('?')
# 0-? (question mark not inclusive)
base_url = url[:question_mark_index]
print(base_url)
# (?+1)-end
params_url = url[question_mark_index + 1:]
print(params_url)
