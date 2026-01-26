import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.tasks = [
            ('My first task', 1),
            ('My second task', 5),
            ('My third task', 10),
        ]
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def add_task(self):
        # name = input('Enter task name: ')
        # priority = int(input('Enter priority: '))

        # self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.c.executemany('INSERT INTO tasks (name, priority) VALUES (?, ?)', self.tasks)
        self.conn.commit()
    
    def read_task(self):
        self.c.execute('SELECT * FROM tasks')
        rows = self.c.fetchall()
        # The fetchall method is less efficient than the iterator, because
        #  it reads all records into the memory and then returns a list of
        #  tuples. For small amounts of data, it doesn't matter, but if
        #  your table contains a huge number of records, this can cause
        #  memory issues.
        for row in rows:
            print(f'from fetchall row is {row}')
        # for row in self.c.execute('SELECT * FROM tasks'):
        #     print(f'row is {row}')
        self.conn.close()
    
    def update_task(self, id, name, priority):
        print(f'updating task with id {id}')
        self.c.execute('UPDATE tasks SET PRIORITY = ? WHERE id = ?', (priority, id))
        self.c.commit()
        self.c.close()
    
    def delete_task(self, id):
        self.c.execute('DELETE FROM tasks WHERE id = ?', (id,))
        self.c.commit()
        self.c.close()


app = Todo()
app.add_task()
app.read_task()


# In addition to the iterator and the fetchall method, the Cursor
#  object provides a very useful method called fetchone to retrieve
#  the next available record. Look at the code in the editor.
# c.execute('SELECT * FROM tasks')
# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)
# conn.close()