"""
Copyright 2022 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
from dataclasses import dataclass
import os


class BaseEnvironment:
    ENV = "base"
    APP_DIR = os.getenv("APP_DIR", os.getcwd())
    PRODUCTION = False


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
