"""
Copyright 2022 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
import os
from config import ProductionEnvironment, \
    DevelopmentEnvironment, TestingEnvironment, BaseEnvironment
from typing import Union
# from peewee import SqliteDatabase


class BaseDatabase:
    def __init__(self, config: Union[DevelopmentEnvironment,
                                     ProductionEnvironment,
                                     BaseEnvironment,
                                     TestingEnvironment]):
        self.db = None

    def get_db(self):
        return self.db


class DatabaseSqlite(BaseDatabase):
    def __init__(self, config):
        super().__init__(config)
        pass
        # self.db = SqliteDatabase(config.SQLITE_PATH, pragmas={'journal_mode': 'wal', })


class AppDatabase:

    _db: dict = dict()

    @staticmethod
    def init_app(app, config):
        sqlite_db = DatabaseSqlite(config)
        app.database = sqlite_db
        AppDatabase._db["sqlite_db"] = sqlite_db

    @staticmethod
    def get_db(name):
        if name not in AppDatabase._db.keys():
            raise ValueError(f"Name {name} database not found")
        return AppDatabase._db[name].get_db()