import webbrowser
class Movie():
    def __init__(self,movie_title,movie_story_line,movie_poster,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_story_line
        self.poster_image_url=movie_poster
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
