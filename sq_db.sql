CREATE TABLE IF NOT EXISTS users (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
email text NOT NULL,
password text NOT NULL,
role TEXT DEFAULT 'user',
time integer NOT NULL
);