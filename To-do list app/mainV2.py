import json
import sys
file_name = "todo-list.json"
def main():
    while True:
        tasks = load_task()
        print("--- TO DO LIST APP MANAGER ---")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Exit")
        choice = str(input("Enter your choice:"))
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            exit()
        else:
            print("Invalid input!")

def add_task(tasks):
    name = str(input("Enter task name:")).strip()
    if name:
        tasks["tasks"].append({"name": name , "complete": False})
        save_task(tasks)
        print("Task added!")
    else:
        print("Name cannot be empty!")
def delete_task(tasks):
    try:
        view_task(tasks)
        idx = int(input("N° of the task:")) - 1
        if 0 <= idx < len(tasks["tasks"]):
            delete_item = tasks["tasks"].pop(idx)
            save_task(tasks)
            print(f"Deleted item : {delete_item('name')}")
        else:
            print("Invalid task number!")
    except:
        print("Invalid input")
def view_task(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("There are no tasks!")
    else:
        for idx , task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['name']} | {status}")
def save_task(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file)
            print("Succesfull saving!")
    except:
        print("Failed saving!")
def load_task():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        print("Failed loading!")
        return {"tasks" : []}
def mark_complete(tasks):
    try:
        view_task(tasks)
        task_number = int(input("Enter the tasks number:"))
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_task(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except:
        print("Invalid input!")
def exit():
    sys.exit()
main()