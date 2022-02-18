import sqlite3
from typing import List


conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()


def get_philosopher(philosopher: str) -> str | None:
    try:
        cursor.execute(f"SELECT bio FROM philosophers "
                       f"WHERE name LIKE '%{philosopher}%'")
        result = cursor.fetchall()
        if len(result) > 1:
            return None
        else:
            result = result[0][0]
    except (TypeError, IndexError):
        return None
    return result


def get_quotes(philosopher_id: int) -> List:
    cursor.execute(f"SELECT quote_text FROM quotes "
                   f"WHERE philosopher_id = {philosopher_id}")
    query = cursor.fetchall()
    quotes = list()
    for obj in query:
        quotes.append(obj[0])
    return quotes
