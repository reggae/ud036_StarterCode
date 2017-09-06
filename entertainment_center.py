import media
import fresh_tomatoes

la_story = media.Movie("L.A. Story",
                       "1h 38m",
                       "Something funny is happening in L.A.",
                       "https://upload.wikimedia.org/wikipedia/en/5/50/Lastoryposter.jpg",
                       "https://www.youtube.com/watch?v=0eCSmfP4g2c")

my_blue_heaven = media.Movie("My Blue Heaven",
                             "1h 37m",
                             "A comedy about a government witness who gives suburbia a culture shock.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/e/ea/My_blue_heaven_poster.jpg/220px-My_blue_heaven_poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=Ci3tBmNxsh0")

three_amigos = media.Movie("Three Amigos",
                           "1h 45m",
                           "Three silent film stars who are mistaken for real heroes "
                           "by the suffering people of a small Mexican village",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/Three_amigos_ver2.jpg/220px-Three_amigos_ver2.jpg",  # noqa
                           "https://www.youtube.com/watch?v=WUTl8DSYUQA")

roxanne = media.Movie("Roxanne",
                      "1h 47m",
                      "This modernization of Edmond Rostand's Cyrano de Bergerac casts Steve Martin as C. D. Bales, "
                      "the fearless, quick-witted fire chief of a Washington State resort town.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Roxanne1987.jpg/250px-Roxanne1987.jpg",
                      "https://www.youtube.com/watch?v=8F-Bwt62qJg")

planes_trains_and_automobiles = media.Movie("Planes, Trains and Automobiles",
                                            "1h 33m",
                                            "Together they must overcome the insanity of holiday travel to reach their "
                                            "intended destination.",
                                            "https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/Planes_trains_and_automobiles.jpg/215px-Planes_trains_and_automobiles.jpg",  # noqa
                                            "https://www.youtube.com/watch?v=VWGqGHMO294")

dirty_rotten_scoundrel = media.Movie("Dirty Rotten Scoundrels",
                                     "1h 50m",
                                     "A story about a competition between con men",
                                     "https://upload.wikimedia.org/wikipedia/en/thumb/2/2c/Dirty_rotten_scoundrels_film.jpg/215px-Dirty_rotten_scoundrels_film.jpg",  # noqa
                                     "https://www.youtube.com/watch?v=lSC2U2yYESw")

# Add above movies to the list of movies
movies = [la_story, my_blue_heaven, three_amigos, roxanne, planes_trains_and_automobiles, dirty_rotten_scoundrel]

# Call fresh tomatoes function open_movies_page with this list of movies
fresh_tomatoes.open_movies_page(movies)

