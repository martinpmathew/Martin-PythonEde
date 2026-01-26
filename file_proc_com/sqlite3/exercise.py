def change_priority(self):
    try:
        task_id = int(input("Enter Task ID to update: "))
        new_priority = int(input("Enter new priority (1 or higher): "))
        
        if new_priority < 1:
            print("Priority must be 1 or greater.")
            return

        sql = 'UPDATE tasks SET priority = ? WHERE id = ?'
        self.cursor.execute(sql, (new_priority, task_id))
        self.conn.commit()
        print("Priority updated successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def delete_task(self):
    try:
        task_id = int(input("Enter Task ID to delete: "))
        sql = 'DELETE FROM tasks WHERE id = ?'
        self.cursor.execute(sql, (task_id,))
        self.conn.commit()
        print("Task deleted successfully.")
    except ValueError:
        print("Invalid ID.")

def main_menu(todo_object):
    while True:
        print("\n--- TODO MENU ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Change Priority")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            todo_object.show_tasks()
        elif choice == '2':
            todo_object.add_task()
        elif choice == '3':
            todo_object.change_priority()
        elif choice == '4':
            todo_object.delete_task()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid selection. Please try again.")

# Objectives

#     improving the student's skills in interacting with the SQLite database;
#     using known SQL statements.

# Scenario

# The application is almost ready. Let's add the missing functionalities to it:

#     Create a method called change_priority, responsible for updating task priority. The method should get the id of the task from the user and its new priority (greater than or equal to 1).
#     Create a method called delete_task, responsible for deleting single tasks. The method should get the task id from the user.
#     Implement a simple menu consisting of the following options:

#     1. Show Tasks 
#     2. Add Task 
#     3. Change Priority 
#     4. Delete Task
#     5. Exit

# where:

#     Show Tasks (calls the show_tasks method)
#     Add Task (calls the add_task method)
#     Change Priority (calls the change_priority method)
#     Delete Task (calls the delete_task method)
#     Exit (interrupts program execution)

# The program should obtain one of these options from the user, and then call the appropriate method of the TODO object. Choosing option 5 must terminate the program. A menu should be displayed in an infinite loop so that the user can choose an option multiple times.