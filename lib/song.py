class Song:
    
    genres = []
    genre_count = {}
    artist_count = {}
    artists = []
    count = 0
    all = []
    
    def __init__(self, name, artist, genre) -> None:
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.all.append(self)
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls):
        unique_genres = set(song.genre for song in cls.all)
        cls.genres = list(unique_genres)

    @classmethod
    def add_to_artists(cls):
        unique_artists = set(song.artist for song in cls.all)
        cls.artists = list(unique_artists)
    
    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count = {}
        for song in cls.all:
            if song.genre in cls.genre_count:
                cls.genre_count[song.genre] += 1
            else:
                cls.genre_count[song.genre] = 1


    @classmethod
    def add_to_artist_count(cls):
        cls.artist_count = {}
        for song in cls.all:
            if song.artist in cls.artist_count:
                cls.artist_count[song.artist] += 1
            else:
                cls.artist_count[song.artist] = 1
      

