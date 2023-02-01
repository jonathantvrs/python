from collections import defaultdict

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
