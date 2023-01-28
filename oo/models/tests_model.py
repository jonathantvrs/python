from model import Movie, Serie, Playlist

avatar = Movie('avatar', 2022, 200)
harry_potter_1 = Movie('harry potter and the philosophers stone', 2001, 159)

everybody_hates_chris = Serie('everybody hates chris', 2005, 4)
my_wife_and_kids = Serie('my wife and kids', 2001, 5)
game_of_thrones = Serie('game of thrones', 2011, 8)

harry_potter_1.like()
game_of_thrones.like()
game_of_thrones.like()
my_wife_and_kids.like()

programs = [game_of_thrones, avatar, everybody_hates_chris, my_wife_and_kids, harry_potter_1]

weekend_playlist = Playlist('Weekend Playlist', programs)


for program in weekend_playlist:
    print(program)