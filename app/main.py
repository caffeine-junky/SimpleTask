from task_manager import TaskManager
from models import TaskStatus
import sys

arguments: list[str] = sys.argv[1:]


def main() -> None:
    """"""
    if len(arguments) == 0:
        return
    manager: TaskManager = TaskManager()

    option: str = arguments[0].lower().strip()

    match option:
        case "add":
            if len(arguments) < 2:
                return
            description: str = arguments[1].strip()
            if not description:
                print("Add a task description...")
                return
            manager.add_task(description)
        case "delete":
            if len(arguments) < 2:
                return
            task_id: str = arguments[1].strip()
            if not task_id.isdigit():
                print("Task id must be a number")
                return
            if manager.remove_task(int(task_id)):
                print(f"Task {task_id} has been removed")
            else:
                print(f"Task {task_id} not found")
        case "update":
            if len(arguments) < 3:
                return
            task_id: str = arguments[1].strip()
            if not task_id.isdigit():
                print("Task id must be a number")
                return
            description: str = arguments[2].strip()
            if not description:
                print("Add a new task description...")
                return
            
            if manager.update_task_description(int(task_id), description):
                print(f"Task {task_id} updated")
            else:
                print(f"Task {task_id} not found")
        case "mark-in-progress" | "mark-done":
            if len(arguments) < 2:
                return
            task_id: str = arguments[1].strip()
            if not task_id.isdigit():
                print("Task id must be a number")
                return
            status = TaskStatus(arguments[0].removeprefix("mark-"))
            if manager.update_task_status(int(task_id), status):
                print(f"Task {task_id} status updated to {status}")
            else:
                print(f"Task {task_id} not found")
        case "list":
            if len(arguments) < 2:
                print("===All Tasks===")
                manager.list_tasks()
            else:
                status_input: str = arguments[1].strip().lower()
                print(f"===Tasks {status_input}===")
                if status_input not in ["todo", "in-progress", "done"]:
                    print(f"Invalid task status: {status_input}")
                else:
                    manager.list_tasks(status=TaskStatus(status_input))
        case _:
            print(f"Invalid option: {option}")


if __name__ == "__main__":
    main()
