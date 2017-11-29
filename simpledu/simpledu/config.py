class BaseConfig(object):
    """config class"""

class DevelopmentConfig(BaseConfig):
    """development configclass"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/simpledu'

class ProductionConfig(BaseConfig):
    """prodcution config class"""
    pass


class TestingConfig(BaseConfig):
    """test envior config class"""
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}