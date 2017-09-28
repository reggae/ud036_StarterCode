class Video:
    """ Stores information shared across all motion picture types,
    including TV shows and Movies """

    def __init__(self, movie_title, duration):
        """ This function will initialize an instance of the class Video"""
        self.title = movie_title
        self.duration = duration


class Movie(Video):
    """ Instances of this Class store a movie's title, storyline, box art
    URL, and YouTube link. """

    def __init__(self, movie_title, duration,
                 movie_storyline, poster_image, trailer_youtube):
        """ This function will initialize an instance of the class Video
        and the subclass Movie"""
        Video.__init__(self, movie_title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
