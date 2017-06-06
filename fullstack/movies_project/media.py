import webbrowser


class Movie():
    """
    Constructer for several instances of movie
    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        movie_title(str): title of movie
        movie_storyline(str): movie stroyline
        poster_image(str): url for poster image
        trailer_youtube(str): url for yt trailer

    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
