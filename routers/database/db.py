#  import logging
import sqlite3

from aiogram import Router

router = Router(name=__name__)


class BotDB:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id          INTEGER PRIMARY KEY,
                            user_id     INTEGER NOT NULL
                                                UNIQUE,
                            name        TEXT,
                            surname     TEXT,
                            father_name TEXT,
                            birthday    TEXT,
                            pervichka   TEXT,
                            photo       TEXT,
                            phone       TEXT
                            )''')

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    # async def cmd_start(self, user_id):
    #     user = self.cur.execute("INSERT INTO users VALUES '{key}'" .format(key=user_id)).fetchone()
    #     if not user:
    #         self.cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (user_id))
    #         self.conn.commit()
    #     return user

    # async def cmd_edit(self, state, user_id):
    #     """Редактирование строки активиста с помощью состояний"""
    #     async with state.proxy() as data:
    #         self.cur.execute("UPDATE users WHERE user_id '{}' SET name '{}', SET surname '{}',"
    #                     " SET father_name '{}', SET birthday '{}', SET pervichka '{}',"
    #                     " SET photo '{}', SET phone '{}' ".format(
    #             user_id, data['name'], data['surname'], data['father_name'],
    #                 data['birthday'], data['pervichka'], data['photo'], data['phone']))
    #         conn.commit()
