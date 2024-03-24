from sqlalchemy import text
from connection.db import Session


with Session.begin() as session:
    session.execute(text('''create table if not exists users( id INTEGER PRIMARY KEY, name TEXT ,username TEXT)'''))
    session.execute(text('''create table if not exists eco( id INTEGER PRIMARY KEY REFERENCES users(id), balance INTEGER)'''))
    session.commit()