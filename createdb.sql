CREATE TABLE IF NOT EXISTS philosophers
(
    philosopher_id integer NOT NULL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    bio TEXT NOT NULL
)