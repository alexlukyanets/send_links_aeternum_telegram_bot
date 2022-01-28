from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, text
from .mixins import MysqlTimestampsMixin, MysqlPrimaryKeyMixin

Base = declarative_base()


class Song(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = 'songs'

    name = Column(VARCHAR(768))
    url = Column(VARCHAR(768), index=True, unique=True)
    keywords = Column(VARCHAR(768))
