#  import logging
import sqlite3


class BotDB:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id     INTEGER PRIMARY KEY
                                                NOT NULL
                                                UNIQUE,
                            surname        TEXT,
                            name     TEXT,
                            father_name TEXT,
                            birthday    TEXT,
                            pervichka   TEXT,
                            photo       TEXT,
                            phone       TEXT,
                            status      INTEGER
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS active_events (
                            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            event_name VARCHAR(100),
                            event_date TEXT,
                            place TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS complete_events (
                            event_id INT PRIMARY KEY,
                            event_name VARCHAR(100),
                            event_date TEXT,
                            place TEXT,
                            event_attedantion INTEGER)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Event_Attendance (
                            attendance_id INTEGER PRIMARY KEY,
                            person_id INTEGER,
                            event_id INTEGER,
                            FOREIGN KEY (person_id) REFERENCES users(user_id),
                            FOREIGN KEY (event_id) REFERENCES active_events(event_id))''')

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `user_id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def name_exists(self, user_id):
        """Проверяем, есть ли имя юзера в базе"""
        result = self.cursor.execute("SELECT 'user_id' FROM users WHERE user_id = ? AND (surname IS"
                                     " NULL OR name IS NULL OR father_name IS NULL)", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `user_id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def get_users(self, status_in_base):
        """Достаем id юзеров в базе по их статусу"""
        result = self.cursor.execute("SELECT user_id FROM users WHERE status <= ?", (status_in_base,))
        return result.fetchall()

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_fullname(self, fullname, user_id):
        parts = fullname.split()
        surname, name, father_name = parts
        self.cursor.execute("UPDATE users SET surname = ?, name = ?, father_name = ? WHERE user_id = ?",
                            (surname, name, father_name, user_id,))
        self.conn.commit()

    def change_user(self, information, ):
        pass

    def get_event(self, active=False, past=False):
        """"Функция достает мероприятия из базы данных"""
        if active:
            result = self.cursor.execute("SELECT event_name, event_date, place FROM active_events")
            return result.fetchall()
        elif past:
            result = self.cursor.execute("SELECT event_name, event_date, place FROM complete_events")
            return result.fetchall()
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
