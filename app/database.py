import os
from config import ProductionEnvironment, DevelopmentEnvironment
from typing import Union
# from peewee import SqliteDatabase

class Database:
    def __init__(self, config: Union[DevelopmentEnvironment, ProductionEnvironment]):
        # self.db = SqliteDatabase(DevelopmentEnvironment.SQLITE_PATH,
        #                          pragmas={'journal_mode': 'wal', })
        self.db = None

    def get(self):
        return self.db

class AppDatabase:

    _db = None

    @staticmethod
    def init_app(app, config: Union[DevelopmentEnvironment, ProductionEnvironment]):
        app.database = AppDatabase._get_db(config)

    @staticmethod
    def get_db():
        return AppDatabase._db

    @staticmethod
    def _get_db(config):
        if AppDatabase._db:
            return AppDatabase._db

        AppDatabase._db = Database(config).get()
        return AppDatabase._db
