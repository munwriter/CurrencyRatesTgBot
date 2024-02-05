import sqlite3 as db
from typing import Optional


class DataBase:
    def __init__(self) -> None:
        with db.connect('currencies.db') as self.db:
            self.cursor = self.db.cursor()

            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                rounding_idx INTEGER,
                source_currency TEXT,
                required_currencies TEXT
                );  
                """
            )
            self.db.commit()

    @staticmethod
    def __format_currencies(curr: str) -> str:
        return ','.join(curr.split())

    def get_user_settings(self, id: int) -> Optional[tuple]:
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def cfg_user_settings(
        self, id: int, rounding_idx: int, source_curr: str, req_curr: str
    ) -> None:
        req_curr = DataBase.__format_currencies(req_curr)
        params = (id, rounding_idx, source_curr, req_curr)
        query = "INSERT OR REPLACE INTO users (id, rounding_idx, source_currency, required_currencies) VALUES (?,?,?,?)"
        self.cursor.execute(query, params)
        self.db.commit()

    def close_connection(self) -> None:
        self.db.close()
