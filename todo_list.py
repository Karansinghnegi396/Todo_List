import os  

def load_task():
    if not os.path.exists("tasks.txt"):
        file = open("tasks.txt", "w")
        file.close()
    
    file = open("tasks.txt", "r")
    content = file.readlines()
    file.close()
    return content

tasks = load_task()
print("Current Tasks:", tasks)

def add_task():
    file = open("tasks.txt", "a")
    task = input("ENTER TASK: ")
    file.write(task + "\n")
    file.close()
    print(f'Task "{task}" added!')

add_task()

def view_tasks():
    tasks = load_task()
    
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for task in tasks:
            print(task.strip())

view_tasks()

def delete_task():
    tasks = load_task()

    if not tasks:
        print("No tasks available to delete.")
        return  

    task_to_delete = input("Enter task to delete: ").strip()
    updated_tasks = [task for task in tasks if task.strip() != task_to_delete]

    if len(updated_tasks) == len(tasks):
        print("Task not found!")
    else:
        file = open("tasks.txt", "w")
        file.writelines(updated_tasks)
        file.close()
        print(f'Task "{task_to_delete}" deleted successfully!')

delete_task()
