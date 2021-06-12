from dataclasses import dataclass
import os


class BaseEnvironment:
    ENV = "base"
    APP_DIR = os.getenv("APP_DIR", os.getcwd())
    PRODUCTION = False

    @staticmethod
    def init_env(env_dict: dict):
        for key, val in env_dict.items():
            os.environ[key] = str(val)

    @staticmethod
    def set_config_name(name):
        _config = {}
        cls = config[name]
        for key in dir(config[name]):
            if key.isupper():
                _config[key] = getattr(cls, key)
        BaseEnvironment.init_env(_config)

    @staticmethod
    def init_app(app):
        BaseEnvironment.init_env(app.config)


class ProductionEnvironment(BaseEnvironment):
    ENV = "production"
    PRODUCTION = True


class DevelopmentEnvironment(BaseEnvironment):
    ENV = "development"


class TestingEnvironment(BaseEnvironment):
    ENV = "testing"


config = {
    "development" : DevelopmentEnvironment,
    "testing" : TestingEnvironment,
    "production": ProductionEnvironment,
    "default" : DevelopmentEnvironment
}
