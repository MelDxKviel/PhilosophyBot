import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()


def get_philosopher(philosopher: str):
    cursor.execute(f"SELECT bio FROM philosophers "
                   f"WHERE name LIKE '%{philosopher}%'")
    try:
        result = cursor.fetchone()[0]
    except TypeError:
        return None
    return result
