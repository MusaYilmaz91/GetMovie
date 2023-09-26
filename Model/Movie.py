class Movie:
    def __init__(self, id:int, ad:str, tur:str,yil:int,sure:str,resimUrl:str,ozet:str):
        self.MovieId =id
        self.MovieName=ad
        self.MovieGenre=tur
        self.MovieYear=yil
        self.MovieTime=sure
        self.MovieUrl=resimUrl
        self.MovieSummary=ozet
        
    def to_dict(self):
        return {
            "film_id": self.MovieId,
            "film_adi": self.MovieName,
            "film_turu": self.MovieGenre,
            "yapim_yili": self.MovieYear,
            "film_suresi": self.MovieTime,
            "resim_url": self.MovieUrl,
            "film_ozeti": self.MovieSummary,
        }