import pyodbc
from Log.log import LoggingHelper

class MsSqlDatabase:
    # Edit database information according to your own database!!
    server = "(LocalDB)\MSSQLLocalDB"
    database = "Filmler"
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    db =pyodbc.connect(connection_string)

    def GetData(script:str,logger_helper:LoggingHelper=None,params:tuple=None):
        #log işlemleri
        if logger_helper==None:
            logger_helper = LoggingHelper()
            logger_helper.create_logger()
        
        logger_helper.log_info("GetData Function is started.")
        try:
            cursor = MsSqlDatabase.db.cursor()
            if params==None:
                cursor.execute(script)
            else:
                cursor.execute(script,params)
            data = cursor.fetchall()
            cursor.close()
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("GetData Function is complete.")
        return data
    
    def AddData(script:str,logger_helper:LoggingHelper=None,params:tuple=None):
        #log işlemleri
        if logger_helper==None:
            logger_helper = LoggingHelper()
            logger_helper.create_logger()

        logger_helper.log_info("AddData Function is started.")
        cursor = MsSqlDatabase.db.cursor()
        try :           
            if params==None:
                cursor.execute(script)
            else:
                cursor.execute(script,params)
            cursor.commit()
            print("İşlem Başarılı.")
        except Exception as e:
            cursor.rollback()
            print("İşlem başarısız oldu!")
            print(e)
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("AddData Function is complete.")

    def DeleteData(table_name:str,kosul:str,logger_helper:LoggingHelper=None,params:tuple=None):
        #log işlemleri
        if logger_helper==None:
            logger_helper = LoggingHelper()
            logger_helper.create_logger()

        logger_helper.log_info("DeleteData Function is started.")
        cursor = MsSqlDatabase.db.cursor()
        sorgu:str=f"DELETE FROM {table_name} WHERE {kosul};"
        try :           
            if params==None:
                cursor.execute(sorgu)
            else:
                cursor.execute(sorgu,params)
            cursor.commit()
            print("İşlem Başarılı.")
        except Exception as e:
            cursor.rollback()
            print("İşlem başarısız oldu!")
            print(e)
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("DeleteData Function is complete.")

    def TruncateTable(table_name:str,logger_helper:LoggingHelper=None,params:tuple=None):
        #log işlemleri
        if logger_helper==None:
            logger_helper = LoggingHelper()
            logger_helper.create_logger()

        logger_helper.log_info("TruncateTable Function is started.")
        cursor = MsSqlDatabase.db.cursor()
        sorgu:str=f"TRUNCATE TABLE {table_name};"
        try :           
            if params==None:
                cursor.execute(sorgu)
            else:
                cursor.execute(sorgu,params)
            cursor.commit()
            print("İşlem Başarılı.")
        except Exception as e:
            cursor.rollback()
            print("İşlem başarısız oldu!")
            print(e)
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("TruncateTable Function is complete.")

    def GetNextId(sorgu:str,logger_helper:LoggingHelper=None):
        #log işlemleri
        if logger_helper==None:
            logger_helper = LoggingHelper()
            logger_helper.create_logger()
        try:
            logger_helper.log_info("GetNextId Function is started.")
            cursor = MsSqlDatabase.db.cursor()
            cursor.execute(sorgu)
            last_id = int(cursor.fetchone()[0])
            next_id = last_id + 1
        except Exception as e:
            logger_helper.log_critical(f"Error encountered: {e}")
        logger_helper.log_info("GetNextId Function is complete.")
        return next_id
