class BaseConfig(object):
    """config class"""
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15

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