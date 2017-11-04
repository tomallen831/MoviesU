import webbrowser


class Video():
    def __init__(self, title, duration, poster_image):
        self.title = title
        self.duration = duration
        self.poster_image_url = poster_image


class Movie(Video):
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, duration, poster_image, movie_storyline,
                 trailer_youtube):
        Video.__init__(self, title, duration, poster_image)
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

        
class TvShow(Video):
    def __init__(self, title, duration, poster_image, season, episode,
                 trailer_youtube):
        Video.__init__(self, title, duration, poster_image)
        self.season = season
        self.episode = episode
        self.trailer_youtube_url = trailer_youtube
