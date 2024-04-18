from sqlalchemy import text
from connection.db import Session


with Session.begin() as session:
    session.execute(text('''create table if not exists users( id INTEGER PRIMARY KEY, name TEXT ,username TEXT)'''))
    session.execute(text('''create table if not exists eco( id INTEGER PRIMARY KEY REFERENCES users(id), balance INTEGER)'''))
    session.execute(text('''create table if not exists user_transactions( id INTEGER PRIMARY KEY, transaction_amount INTEGER, transaction_type TEXT, user_id INTEGER REFERENCES users(id))'''))
    session.execute(text('''create table if not exists user_logi( id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES users(id), date_time TEXT, command TEXT)'''))
    session.execute(text('''create table if not exists user_who(id INTEGER PRIMARY KEY, user_id  INTEGER REFERENCES users(id), message_id INTEGER, chat_id INTEGER, result TEXT)'''))
    session.commit()