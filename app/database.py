import os

class Database:
    def __init__(self):
        pass

class AppDatabase:

    _db = None

    @staticmethod
    def init_app(app):
        app.database = AppDatabase.get_db(app.config)

    @staticmethod
    def get_db(config: dict):
        if AppDatabase._db is None:
            AppDatabase._db = Database()
        return AppDatabase._db
