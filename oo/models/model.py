class Program:
    def __init__(self, name, year):
        self.__name = name.title()
        self.year = year
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1

    def __str__(self):
        return f'{self.name} - {self.likes} Likes'

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration
        
    def __str__(self):
        return f'{self.name} - {self.duration} min - {self.likes} Likes'

class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - {self.seasons} seasons - {self.likes} Likes'


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self.__programs = programs

    def __getitem__(self, index):
        return self.__programs[index]

    def __len__(self):
        return len(self.__programs)