from model import Movie

harry_potter_1 = Movie('Harry Potter and the Philosopher\'s Stone', \
    'Chris Columbus')
harry_potter_2 = Movie('Harry Potter and the Chamber of Secrets', \
    'Chris Columbus')

my_movies_list = [harry_potter_1, harry_potter_2]

for movie in my_movies_list:
    print(movie)

hp1 = Movie('Harry Potter and the Philosopher\'s Stone', \
    'Chris Columbus')

# Print True because the __eq__ method has been implemented for comparison
# The in operator is based on the == operator 
print(hp1 in my_movies_list) # print True
print(hp1 == my_movies_list[0]) # print True

