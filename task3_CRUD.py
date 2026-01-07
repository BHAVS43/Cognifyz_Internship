class Task:
    def __init__(self, name):
        self.name = name


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        name = input("Enter task: ")
        task = Task(name)
        self.tasks.append(task)
        print("Task added")

    def read_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available")
        else:
            for i in range(len(self.tasks)):
                print(i + 1, ".", self.tasks[i].name)

    def update_task(self):
        try:
            num = int(input("Enter task number to update: "))
            if num > 0 and num <= len(self.tasks):
                new_name = input("Enter new task: ")
                self.tasks[num - 1].name = new_name
                print("Task updated")
            else:
                print("Invalid task number")
        except:
            print("Please enter a valid number")

    def delete_task(self):
        try:
            num = int(input("Enter task number to delete: "))
            if num > 0 and num <= len(self.tasks):
                self.tasks.pop(num - 1)
                print("Task deleted")
            else:
                print("Invalid task number")
        except:
            print("Please enter a valid number")


manager = TaskManager()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.create_task()
    elif choice == "2":
        manager.read_tasks()
    elif choice == "3":
        manager.update_task()
    elif choice == "4":
        manager.delete_task()
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
