class Config(object):
    """
    Configurações comuns em todo o ambiente
    """



class DevelopmentConfig(Config):
    """
    Configurações de desenvolvimento
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Configurações de produção
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}