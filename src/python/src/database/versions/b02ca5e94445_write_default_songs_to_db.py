"""write default songs to db

Revision ID: b02ca5e94445
Revises: df416969bb3c
Create Date: 2022-01-28 17:13:41.885943

"""
import csv

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql
from database.models.song import Song
from database.mysql_connection_string import mysql_connection_string
from sqlalchemy.dialects.mysql import insert

# revision identifiers, used by Alembic.
revision = 'b02ca5e94445'
down_revision = 'df416969bb3c'
branch_labels = None
depends_on = None

file = open('default_data/songs.csv', encoding="utf-8")
csvreader = csv.reader(file)
engine = sa.create_engine(mysql_connection_string())


def upgrade():
    with engine.connect() as connection:
        for row in csvreader:
            if not row:
                continue
            keywords = row[0].lower()
            if len(row) == 3:
                keywords = f'{keywords}.{row[2]}'
            song_dict = {'name': row[0],
                         'url': row[1],
                         'keywords': keywords}

            inseted_stmt = insert(Song)
            stmt = inseted_stmt.on_duplicate_key_update(url=song_dict.get('url')).values(song_dict)
            connection.execute(stmt)


def downgrade():
    pass
