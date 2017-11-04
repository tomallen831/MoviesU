import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story", "120 minutes",
    "https://upload.wikimedia.org/wikipedia/commons/4/46/Toy_Story.svg",
    "A story of toys",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "120 minutes",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "A marine on an alien planet",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie(
    "School of Rock",
    "120 minutes",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "Using Rock to Learn", "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatoullie = media.Movie(
    "Ratatoullie",
    "120 minutes",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "A rat's a chef",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

The_fast_and_the_furious = media.Movie(
    "The Fast and the Furious",
    "120 minutes",
    "https://upload.wikimedia.org/wikipedia/en/5/54/Fast_and_the_furious_poster.jpg",
    "An amazing story of street racers",
    "https://www.youtube.com/watch?v=ZsJz2TJAPjw")

Seinfeld = media.TvShow(
    "Seinfeld",
    "30 minutes",
    "https://upload.wikimedia.org/wikipedia/commons/7/78/Seinfeld_logo.svg",
    "Season 1",
    "Episode 1",
    "https://www.youtube.com/watch?v=PaPxSsK6ZQA")

movies = [ratatoullie, The_fast_and_the_furious, toy_story, avatar, school_of_rock,
          Seinfeld]

fresh_tomatoes.open_movies_page(movies)
