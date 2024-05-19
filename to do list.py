tasks = []

def add_task():
    num_tasks = int(input("How many tasks  want to add: "))
    for _ in range(num_tasks):
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
    print("Tasks added!")

def show_tasks():
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['task']} {'Done' if task['done'] else 'Not Done'}")

def mark_task_done():
    show_tasks()
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List\n1. Add Task\n2. Show Tasks\n3. Mark Task as Done\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        mark_task_done()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")