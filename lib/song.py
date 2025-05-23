class Song:
    count = 0
    genres = []
    artists = []
    genre_count = []
    artist_count = []
    
    def __init__(self, name, artist, genre, count):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.genres.append(genre)
        Song.artist.append(artist)
        Song.count.append(<1=[0])

        Song.add_to_genres()
        Song.add_to_artists()
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1                 
         

    