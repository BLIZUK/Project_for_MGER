#  import logging
import sqlite3

from aiogram import Router

router = Router(name=__name__)

conn = sqlite3.connect("")
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER,
    block INTEGER);
    """)
conn.commit()

# class diolog(StatesGroup):
