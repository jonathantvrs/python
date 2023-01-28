class Movie:
    def __init__(self, name, director):
        self.name = name 
        self.director = director

    def __str__(self):
        return f'{self.name} - {self.director}'

    def __eq__(self, another_movie):
        return self.name == another_movie.name and \
            self.director == another_movie.director