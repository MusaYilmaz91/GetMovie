import requests,json
from MovieDBService import MovieServices
from bs4 import BeautifulSoup
from Model.Movie import Movie
from MsSqlDatabase import MsSqlDatabase
from Log.log import LoggingHelper

logger_helper = LoggingHelper()

class BringMovieFeatures:

    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
                        "Referer": "https://www.google.com"
                } 
    def htmlrequest():
        try:
            id=int(input("1-24277 arasından bir sayı girin: "))
            if id<=0 or id>24277:
                id =1
        except ValueError:
            id=1 
            pass
        data=MovieServices.GetMovieLink(id,logger_helper)
        url=data.Link
        response = requests.get(url,headers=BringMovieFeatures.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
        
    def GetMovieName():
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieName function is started.")
        try:
            film_adi = BringMovieFeatures.htmlrequest().find('div', class_='titlebar-title titlebar-title-lg').text
        except Exception as e:
            print(e)
            logger_helper.log_info(f"error encountered: {e}")
        print(film_adi)
        logger_helper.log_info("GetMovieName function is complete.")
        return str(film_adi)
    
    def GetMovieYear():
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieYear function is started.")
        try:
            span_etiketi=BringMovieFeatures.htmlrequest().find('span', string='Yapım yılı')
            yapim_yili = int(span_etiketi.find_next_sibling('span', class_='that').text)
        except Exception as e:
            print(e)
            yapim_yili=0
            logger_helper.log_info(f"error encountered: {e}")
            pass
        print(yapim_yili)
        logger_helper.log_info("GetMovieYear function is complete.")
        return yapim_yili
    
    def GetMoviePictureUrl():
        logger_helper.create_logger()
        logger_helper.log_info("GetMoviePictureUrl function is started.")
        try:
            resim1_gecici=BringMovieFeatures.htmlrequest().find('a',class_='shot-item')
            resim_url1_gecici=resim1_gecici.get('href')
            get_image=requests.get("https://www.beyazperde.com"+resim_url1_gecici,headers=BringMovieFeatures.headers)
            ara=BeautifulSoup(get_image.text,'html.parser')
            source_etiketi = ara.find('source', attrs={'media': '(min-width: 64em)'})
            resim_url = str(source_etiketi.get('srcset'))
        except Exception as e:
            print(e)
            resim_url="-"
            logger_helper.log_info(f"error encountered: {e}")
            pass
        print(resim_url)
        logger_helper.log_info("GetMoviePictureUrl function is complete.")
        return str(resim_url)
    
    def GetMovieTime():
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieTime function is started.")
        try:
            sure_gecici=BringMovieFeatures.htmlrequest().find('div', class_='meta-body-item meta-body-info').find('span', class_='spacer').find_next_sibling(string=True)
            sure = sure_gecici.strip()
            if sure ==""or None:
                sure="-"
        except Exception as e:
            print(e)
            sure="-"
            logger_helper.log_info(f"error encountered: {e}")
            pass
        print(sure)
        logger_helper.log_info("GetMovieTime function is complete.")
        return str(sure)
    
    def GetMovieGenre():
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieGenre function is started.")
        try:
            tur_gecici = BringMovieFeatures.htmlrequest().find('script',type="application/ld+json")
            data_analiz=json.loads(tur_gecici.string)
            tur=str(data_analiz['genre'])
            if "[" in tur:
                tur=data_analiz['genre']
                tur =', '.join(tur)
        except Exception as e:
            print(e)
            tur = "-"
            logger_helper.log_info(f"error encountered: {e}")
            pass
        print(tur)
        logger_helper.log_info("GetMovieGenre function is complete.")
        return tur
    
    def GetMovieSummary():
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieSummary function is started.")
        try:
            ozet=BringMovieFeatures.htmlrequest().find('div',class_="content-txt").text
            if ozet == None:
                ozet=""
            else:
                ozet=ozet.strip()
        except Exception as e:
            print(e)
            ozet="-"
            logger_helper.log_info(f"error encountered: {e}")
            pass
        print(ozet)
        logger_helper.log_info("GetMovieSummary function is complete.")
        return str(ozet)
    
    def GetMovieAllFeatures():
        logger_helper.create_logger()
        logger_helper.log_info("GetMovieAllFeatures function is started.")
        soup=BringMovieFeatures.htmlrequest()
        try:
            film_adi = soup.find('div', class_='titlebar-title titlebar-title-lg').text
        except Exception as e:
            print(e)
            film_adi="-"
            logger_helper.log_info(f"error encountered: {e}")
        try:
            span_etiketi=soup.find('span', string='Yapım yılı')
            yapim_yili = int(span_etiketi.find_next_sibling('span', class_='that').text)
        except Exception as e:
            print(e)
            yapim_yili=0
            logger_helper.log_info(f"error encountered: {e}")
            pass
        try:
            resim1_gecici=soup.find('a',class_='shot-item')
            resim_url1_gecici=resim1_gecici.get('href')
            get_image=requests.get("https://www.beyazperde.com"+resim_url1_gecici,headers=BringMovieFeatures.headers)
            cevap_html=get_image.text
            ara=BeautifulSoup(cevap_html,'html.parser')
            source_etiketi = ara.find('source', attrs={'media': '(min-width: 64em)'})
            resim_url = str(source_etiketi.get('srcset'))
        except Exception as e:
            print(e)
            resim_url="-"
            logger_helper.log_info(f"error encountered: {e}")
            pass
        try:
            sure_gecici=soup.find('div', class_='meta-body-item meta-body-info').find('span', class_='spacer').find_next_sibling(string=True)
            sure = sure_gecici.strip()
            if sure ==""or None:
                sure="-"
        except Exception as e:
            print(e)
            sure="-"
            logger_helper.log_info(f"error encountered: {e}")
            pass
        try:
            tur_gecici = soup.find('script',type="application/ld+json")
            data=tur_gecici.string
            data_analiz=json.loads(data)
            tur=str(data_analiz['genre'])
            if "[" in tur:
                tur=data_analiz['genre']
                tur =', '.join(tur)
        except Exception as e:
            print(e)
            tur = "-"
            logger_helper.log_info(f"error encountered: {e}")
            pass
        try:
            ozet=soup.find('div',class_="content-txt").text
            if ozet == None:
                ozet=""
            else:
                ozet=ozet.strip()
        except Exception as e:
            print(e)
            ozet="-"
            logger_helper.log_info(f"error encountered: {e}")
            pass

        next_id=MsSqlDatabase.GetNextId("SELECT MAX(film_id) FROM [Filmler].[dbo].[Film_Ozellikleri];",logger_helper)
        movie=Movie(next_id,film_adi,tur,yapim_yili,sure,resim_url,ozet)
        logger_helper.log_info("GetMovieAllFeatures function is complete.")
        return movie