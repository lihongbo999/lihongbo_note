class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(ProdConfig):
    DEBUG = True



