import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_FOLDER = os.getenv("APP_FOLDER", "/usr/src/app")
    STATIC_FOLDER = f"{APP_FOLDER}/project/static"
    MEDIA_FOLDER = f"{APP_FOLDER}/project/media"
