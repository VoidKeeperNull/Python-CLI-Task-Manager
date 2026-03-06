import argparse
import json

try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = {}

parser = argparse.ArgumentParser(description='A task management system made in Python. Created by VKN.')
meg = parser.add_mutually_exclusive_group()
meg.add_argument('--new', help='Create a new task', action="store_true")
meg.add_argument('--edit', help='Edit an existing task', action="store_true")
meg.add_argument('--complete','-c', help='Mark task as complete', action="store_true")
meg.add_argument('--delete','-dl', help='Delete a task', action="store_true")
meg.add_argument('--list', help='List all tasks', action="store_true")
parser.add_argument('-n','--name', type=str, help='Task Name')
parser.add_argument('-d','--description', type=str, help='Task Description')
parser.add_argument('-p','--priority', type=int, help='Task Priority')
parser.add_argument('-s','--status', type=str, help='Task Status')

args = parser.parse_args()
if args.new:
    if not args.name in tasks:
        tasks[args.name] = {"description": args.description, "priority": args.priority, "status": args.status}
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=3)
    else:
        print(f'Task "{args.name}" already exists. Task not saved.')
elif args.edit:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    new_description = args.description if args.description is not None else tasks.get(args.name, {}).get("description", "")
    new_priority = args.priority if args.priority is not None else tasks.get(args.name, {}).get("priority", 1)
    new_status = args.status if args.status is not None else tasks.get(args.name, {}).get("status", "Not Started")
    tasks[args.name] = {"description": new_description, "priority": new_priority, "status": new_status}
    confirm=input(f'Editing task: {args.name}, Description: {new_description}, Priority: {new_priority}, Status: {new_status}. Type Y and Enter to save changes. ')
    if confirm.lower() == 'y':
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=3)
    else:
        print('Changes not saved.')
elif args.complete:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    tasks[args.name]["status"] = "Complete"
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=3)
elif args.delete:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    if args.name in tasks:
        del tasks[args.name]
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=3)
    else:
        print(f'Task "{args.name}" not found.')
elif args.list:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    if args.name:
        task = tasks.get(args.name)
        if task:
            print(f'Task: {args.name}, Description: {task["description"]}, Priority: {task["priority"]}, Status: {task["status"]}')
        else:
            print(f'Task "{args.name}" not found.')
    else:
        for name, details in tasks.items():
            print(f'Task: {name}, Description: {details["description"]}, Priority: {details["priority"]}, Status: {details["status"]}')
