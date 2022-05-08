import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:morces@localhost/pitches'
    

class DevConfig(Config):


    DEBUG = True

class ProdConfig(Config):


    pass 


config_options = {
    'development':DevConfig,
    'production' :ProdConfig
}