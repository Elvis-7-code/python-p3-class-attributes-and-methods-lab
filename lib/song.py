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
    def add_song_to_count(cls)
        cls.count += 1

    # @classmethod
    # def add_to_genres    
         

    