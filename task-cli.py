import argparse
import json
import os
from datetime import datetime

# JSON file path
TASKS_FILE = "tasks.json"

def load_tasks() :
    """
    JSON으로부터 파일을 읽어옵니다.
    파일이 없다면 빈 목록을 return 합니다.
    """
    if os.path.exists(TASKS_FILE) :
        with open(TASKS_FILE, "r") as file :
            return json.load(file)
    return []

def save_tasks(tasks) :
    """
    목록을 JSON 파일에 저장합니다.
    """
    with open(TASKS_FILE, "w") as file :
        json.dump(tasks, file, indent=4)

def add_task(description) :
    """
    새로운 작업을 추가하고 저장합니다.

    description : 작업에 저장될 내용
    """
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added sucessfully (ID: {task_id})")

def list_tasks(status=None) :
    """
    작업 목록을 출력합니다.
    상태별로 필터링이 가능합니다.

    status : 필터링할 작업 상태, 디폴트는 None
    """
    tasks = load_tasks()
    if not tasks :
        print("No tasks found.")
        return
    for task in tasks :
        if(task['status'] == status or status == None) :
            print(f"[{task['id']}] {task['description']} / {task['status']} (create : {task['createdAt']}, last update : {task['updatedAt']})")

def update_task(task_id, new_description) :
    """
    기존 작업의 설명을 업데이트 후 저장합니다.

    task_id : 업데이트할 작업의 ID
    new_description : 새로운 작업 설명명
    """
    tasks = load_tasks()
    for task in tasks :
        if task['id'] == task_id :
            task['description'] = new_description
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")


def delete_task(task_id) :
    """
    선택한 작업을 삭제하고 ID를 정렬 후, 저장합니다.

    task_id : 삭제할 작업의 ID
    """
    tasks = load_tasks()
    for task in tasks :
        if task['id'] == task_id :
            tasks.remove(task)
            for idx, task in enumerate(tasks) :
                task['id'] = idx+1
            save_tasks(tasks)
            print(f"Task deleted successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")


def change_task_status(task_id, new_status) :
    """
    선택한 작업의 상태를 변경합니다.

    task_id : 상태를 변경할 작업의 ID
    new_status : 새로운 작업 상태
    """
    tasks = load_tasks()
    for task in tasks :
        if task['id'] == task_id :
            task['status'] = new_status
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task status changed to {new_status} (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found.")


def main() :
    """
    CLI 구조를 설정하고 명령어를 처리합니다.
    """

    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task to add")

    # list command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("status", type=str, nargs="?", choices=["todo", "in-progress", "done"], help="Filter tasks by status")

    # update command
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="The Id of the task to update")
    update_parser.add_argument("description", type=str, help="The new description of the task")

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an existing task")
    delete_parser.add_argument("id", type=int, help="The ID of the taks to delete")

    # mark-in-progress command
    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    mark_in_progress_parser.add_argument("id", type=int, help="The ID of the task to mark as in progress")

    # mark-done command
    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("id", type=int, help="The ID of the task to mark as done")

    args = parser.parse_args()

    if args.command == "add" :
        add_task(args.task)
    elif args.command == "list" :
        list_tasks(args.status)
    elif args.command == "update" :
        update_task(args.id, args.description)
    elif args.command == "delete" :
        delete_task(args.id)
    elif args.command == "mark-in-progress" :
        change_task_status(args.id, "in-progress")
    elif args.command == "mark-done" :
        change_task_status(args.id, "done")
    else :
        parser.print_help()

if __name__ == "__main__" :
    main()