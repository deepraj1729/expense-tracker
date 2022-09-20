
class XpenseConfig:
    @staticmethod
    def buildPATH(path, filename):
        return path+filename
    
    @staticmethod
    def buildURL(url, endpoint):
        return url+endpoint

    class DB:
        DB_TYPE = "mongodb"
        DB_NAME = "xpense_db"
        DB_COLLECTION_NAME = "xpense_collection"
        DB_CONN_URL = "mongodb://localhost:27017/"
        DB_CONN_PROD_URL = ""
        DB_ABSTR_TYPE = "ORM"
        DB_ABSTR_FRM = "SQLAlchemy"

    
    class Monitoring:
        MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    
    class API:
        DEV_URL= "http://0.0.0.0:8000"
        PROD_URL="https://xpense-api.herokuapp.com"
        ENDPOINTS = {
            "add":"/add",
            "create":"/create",
            "update":"/update",
            "delete":"/delete",
            "analyze":"/analyze"}
        
        API_KEYS = [
            "akljnv13bvi2vfo0b0bw"
        ]
        
        CORS_ORIGINS = [
            "http://localhost:8080",
            "http://localhost:3000",
            "http://localhost:4000"
        ]
    
    class IO:
        OUTPUT = "./output/"
        LOGS_PATH = "./logs/"