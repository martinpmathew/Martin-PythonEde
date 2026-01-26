import sqlite3

conn = sqlite3.connect("hello.db")
# conn = sqlite3.connect(':memory:') # :memory:, which creates a database in RAM
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          priority INTEGER NOT NULL
          );''')
c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)', ("First Task", 1))
conn.commit()
conn.close()
