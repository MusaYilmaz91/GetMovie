import logging,datetime

class LoggingHelper:
    def __init__(self):
        self.logFormati = '%(asctime)s - %(levelname)s - %(message)s'
        self.logSeviyesi = logging.DEBUG
        self.logger = logging.getLogger()
        self.logger.setLevel(self.logSeviyesi)

    def create_logger(self):
        su_an = datetime.datetime.now()
        tarih_formati = "%d-%m-%Y"
        saat_formati = "%H-%M-%S"
        tarih_yazdir = su_an.strftime(tarih_formati)
        saat_yazdir = su_an.strftime(saat_formati)
        date_time = f"{tarih_yazdir}_{saat_yazdir}.log"
        logDosyaAdi = f"C:\\Users\\MusaYilmaz\\Desktop\\mssql_projesi\\Log\\{date_time}"

        formatter = logging.Formatter(self.logFormati)

        file_handler = logging.FileHandler(logDosyaAdi)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self,message):
        self.logger.critical(message)

