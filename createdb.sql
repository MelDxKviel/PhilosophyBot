CREATE TABLE IF NOT EXISTS philosophers
(
    philosopher_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64) NOT NULL,
    bio TEXT NOT NULL
)