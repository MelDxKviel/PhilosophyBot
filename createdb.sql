CREATE TABLE IF NOT EXISTS philosophers
(
    philosopher_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64) NOT NULL,
    bio TEXT NOT NULL,
    image_link VARCHAR(255),
    wiki_link VARCHAR(255) NOT NULL,
);

CREATE TABLE IF NOT EXISTS quotes
(
   quote_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   quote_test TEXT NOT NULL,
   philosopher_id INTEGER NOT NULL,
   FOREIGN KEY (philosopher_id) REFERENCES philosophers(philosopher_id)
);