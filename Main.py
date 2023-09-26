from MovieDBService import MovieServices 
from GetMovieFromHttp import BringMovieFeatures as BMF
from JSONFormatter import JSONFormatter as js
from MsSqlDatabase import MsSqlDatabase

# YOU CAN TRY THE CODES BELOW

# movie_list=MovieServices.GetAllMovie()
# print(js.convert(movie_list))
# for movie in movie_list:
#     print(str(movie.MovieId)+":"+movie.MovieName)
#     # if movie.MovieId==3:
#     #     print(movie.MovieName)


# movie=MovieServices.GetMovieById(3)
# print(movie.MovieName)


# movie_links=MovieServices.GetMovieAllLinks()
# #print(js.convert(movie_links))
# for link in movie_links:
#     print(link.LinkId)



# movie_link=MovieServices.GetMovieLink(61)
# print(movie_link.Link)



# BMF.GetMovieName()


# BMF.GetMovieGenre()


# BMF.GetMovieSummary()


# BMF.GetMovieTime()


# BMF.GetMoviePictureUrl()


# BMF.GetMovieYear()


# movie=BMF.GetMovieAllFeatures()
# print(movie.MovieUrl)


# movie2=BMF.GetMovieSummary()
# print(movie2)

