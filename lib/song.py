class Song:
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_tocount()
        Song.genres.append(genre)
        Song.artist.append(artist)

        Song.add_to_genres()
        Song.add_to_artists()
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls): 
        cls.genres = list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls.artists))   

    @classmethod
    def add_to_genres_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1   

    @classmethod
    def add_to_artists_count(cls, artists):
        if artist in cls.artists_count:
            cls.artists_count[artists] += 1
        else:
            cls.artists_count[artist] = 1                     
         

    