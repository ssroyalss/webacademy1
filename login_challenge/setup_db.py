import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT)')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('salman', '123123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user2', 'mypassword')")

connection.commit()
connection.close()