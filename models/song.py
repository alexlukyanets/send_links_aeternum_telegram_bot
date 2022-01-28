from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, text

Base = declarative_base()


class Song(Base):
    __tablename__ = 'songs'

    id = Column("id", BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(768))
    url = Column(VARCHAR(768), index=True, unique=True)
    keywords = Column(VARCHAR(768))
    created_at = Column(
        "created_at", TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at = Column(
        "updated_at",
        TIMESTAMP,
        nullable=False,
        index=True,
        unique=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP"),
    )
