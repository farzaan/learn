import media
import fresh_tomatoes


# Creating the movie intances
toy_story = media.Movie(
    "Toy Story",
    "A story of a young boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio"
    )

avatar = media.Movie(
    "Avatar",
    "A story about a marine on a planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

inception = media.Movie(
    "Inception",
    "A story of a young boy and a mean world",
    "https://images-na.ssl-images-amazon.com/images/I/61Ug%2BK8o5FL.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0"
    )

forrest_gump = media.Movie(
    "Forrest Gump",
    "A story of a young boy and his adventures in life",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg"
    )


# Adding the movie intances to the movies list
movies = []

movies.append(toy_story)
movies.append(avatar)
movies.append(inception)
movies.append(forrest_gump)

# Lets display the movies page
fresh_tomatoes.open_movies_page(movies)
