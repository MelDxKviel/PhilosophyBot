import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()


def get_philosopher(philosopher: str) -> dict | None:
    try:
        cursor.execute(f"SELECT philosopher_id, name, bio, image_link, wiki_link FROM philosophers "
                       f"WHERE name LIKE '%{philosopher}%'")
        result = cursor.fetchall()
        if len(result) > 1:
            return None
        else:
            result = result[0]
            data = {
                "id": result[0],
                "name": result[1],
                "bio": result[2],
                "image_link": result[3],
                "wiki_link": result[4]
            }
    except (TypeError, IndexError):
        return None
    return data


def get_quotes(philosopher_id: int) -> list:
    cursor.execute(f"SELECT quote_text FROM quotes "
                   f"WHERE philosopher_id = {philosopher_id}")
    query = cursor.fetchall()
    quotes = list()
    for obj in query:
        quotes.append(obj[0])
    return quotes
