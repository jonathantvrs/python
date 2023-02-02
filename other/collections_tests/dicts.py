from collections import Counter, defaultdict

counting_words = {}
print(type(counting_words))
counting_words = dict()
print(type(counting_words))

counting_words = {
    'table': 0,
    'book': 0,
    'deskpad': 0
}

text = 'the book is on the table'

for word in text.split():
    if word in counting_words:
        counting_words[word] += 1

for k, v in counting_words.items():
    print(f'key: {k}, value: {v}')

counting_words = defaultdict(int)

for word in text.split():
    counting_words[word] += 1

for k, v in counting_words.items():
    print(f'key: {k}, value: {v}')

counting_words = Counter(text.split())
for k, v in counting_words.items():
    print(f'key: {k}, value: {v}')

print(counting_words.most_common(1))

my_contacts = {'Ary': 123, 'Ana': 456, 'Roberto': 789}
ana_contacts = {'Joelma': 222, 'Arthur': 444}
# extending my contacts with ana contacts
my_contacts.update(ana_contacts)
print(my_contacts)