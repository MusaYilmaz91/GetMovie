from MsSqlDatabase import MsSqlDatabase
from Model.Movie import Movie
from Model.MovieLink import MovieLink
from typing import List
from Log.log import LoggingHelper

logger_helper = LoggingHelper()

class MovieServices:

    def GetMovieById(id:int)->Movie:
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieById Function is started.")
        try:
            sorgu:str=f"SELECT film_id,film_adi,film_turu,yapim_yili,film_suresi,resim_url,film_ozeti  FROM [Filmler].[dbo].[Film_Ozellikleri] WHERE film_id= ?;"
            data=MsSqlDatabase.GetData(sorgu,logger_helper,id)
            for row in data:
                movie = Movie(*row) 
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("GetMovieById Function is complete.")
        return movie
    
    def GetAllMovie()->List[Movie]:
        logger_helper.create_logger()
        logger_helper.log_info("GetAllMovie Function is started.")
        try:
            sorgu:str=f"SELECT * FROM [Filmler].[dbo].[Film_Ozellikleri];"
            data=MsSqlDatabase.GetData(sorgu,logger_helper)
            movies = []
            for row in data:
                movie = Movie(*row) 
                movies.append(movie)
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("GetAllMovie Function is complete.")
        return movies
    
    def GetMovieLink(id:int,logger_helper:LoggingHelper=None)->MovieLink:
        if logger_helper==None:
            logger_helper = LoggingHelper()
            logger_helper.create_logger()
        logger_helper.log_info("GetMovieLink Function is started.")
        try:
            sorgu:str = f"SELECT id,url FROM [Filmler].[dbo].[Film_Linkleri] WHERE id= ?;"
            data=MsSqlDatabase.GetData(sorgu,logger_helper,id)
            for row in data:
                link = MovieLink(*row) 
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("GetMovieLink Function is complete.")
        return link
        
    def GetMovieAllLinks()->List[MovieLink]:
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieAllLink Function is started.")
        try:
            sorgu:str = "SELECT id,url FROM [Filmler].[dbo].[Film_Linkleri];"
            data=MsSqlDatabase.GetData(sorgu,logger_helper)
            movie_links=[]
            for row in data:
                link = MovieLink(*row) 
                movie_links.append(link)
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("GetMovieAllLink Function is complete.")
        return movie_links
    
    def AddMovie(movie:Movie):
        logger_helper.create_logger()
        logger_helper.log_info("AddMovie Function is started.")
        try:
            next_id=MsSqlDatabase.GetNextId("SELECT MAX(film_id) FROM [Filmler].[dbo].[Film_Ozellikleri];")
            sorgu =f"INSERT INTO [Filmler].[dbo].[Film_Ozellikleri] (film_id,film_adi, film_turu, yapim_yili, film_suresi, resim_url, film_ozeti) VALUES (?, ?, ?, ?, ?, ?, ?);"
            veri = (next_id,movie.MovieName, movie.MovieGenre, movie.MovieYear, movie.MovieTime, movie.MovieUrl, movie.MovieSummary)
            MsSqlDatabase.AddData(sorgu,logger_helper,veri)
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("AddMovie Function is complete.")

    def AddMovieList(movieList:List[Movie]):
        logger_helper.create_logger()
        logger_helper.log_info("AddMovieList Function is started.")
        try:
            for movie in movieList:
                next_id=MsSqlDatabase.GetNextId("SELECT MAX(film_id) FROM [Filmler].[dbo].[Film_Ozellikleri];")
                sorgu =f"INSERT INTO [Filmler].[dbo].[Film_Ozellikleri] (film_id,film_adi, film_turu, yapim_yili, film_suresi, resim_url, film_ozeti) VALUES (?, ?, ?, ?, ?, ?, ?);"
                veri = (next_id,movie.MovieName, movie.MovieGenre, movie.MovieYear, movie.MovieGenre, movie.MovieUrl, movie.MovieSummary)
                MsSqlDatabase.AddData(sorgu,logger_helper,veri)
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("AddMovieList Function is complete.")

    def AddMovieLink(url:str):
        logger_helper.create_logger()
        logger_helper.log_info("AddMovieLink Function is started.")
        try:
            next_id=MsSqlDatabase.GetNextId("SELECT MAX(id) FROM [Filmler].[dbo].[Film_Linkleri];")
            sorgu:str =f"INSERT INTO [Filmler].[dbo].[Film_Linkleri] (id,url) VALUES (?,?);" 
            veri=next_id,url
            MsSqlDatabase.AddData(sorgu,logger_helper,veri)
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("AddMovieLink Function is complete.")
    
    def UpdateMovie(id:int,film_adi:str, tur:str, yapim_yili:int, sure:str, resim_url:str, ozet:str):
        logger_helper.create_logger()
        logger_helper.log_info("UpdateMovie Function is started.")
        try:
            sorgu:str=f"UPDATE [Filmler].[dbo].[Film_Ozellikleri] SET film_adi = ?, film_turu = ?, yapim_yili = ?,film_suresi = ?, resim_url = ?, film_ozeti = ? WHERE film_id = ?"
            veri=film_adi,tur,yapim_yili,sure,resim_url,ozet,id
            MsSqlDatabase.AddData(sorgu,logger_helper,veri)
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("UpdateMovie Function is complete.")
    
    def UpdateMovieLink(id:int,url:str):
        logger_helper.create_logger()
        logger_helper.log_info("UpdateMovieLink Function is started.")
        try:
            sorgu:str=f"UPDATE [Filmler].[dbo].[Film_Linkleri] SET url = ? WHERE id = ?"
            veri=url,id
            MsSqlDatabase.AddData(sorgu,logger_helper,veri)
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("UpdateMovieLink Function is complete.")
