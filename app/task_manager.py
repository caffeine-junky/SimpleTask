from models import Task, TaskStatus
from pathlib import Path
import json


class TaskManager:

    def __init__(self) -> None:
        self._db_path: Path = Path(__file__).resolve().parent / "task_db.json"
        self._tasks: list[Task] = []
        
        self.initialize_db()
    
    def initialize_db(self) -> None:
        """"""
        if self._db_path.exists():
            with open(self._db_path, "r") as file:
                data = json.load(file)
                self._tasks = [Task(**task) for task in data]
        else:
            self._db_path.touch()

            with open(self._db_path, "w") as file:
                json.dump([], file, indent=4)
    
    def add_task(self, description: str) -> None:
        """"""
        task: Task = Task(id=self._generate_id(), description=description)
        self._tasks.append(task)
        self._save_db()
        
        print(f"Task added successfully (ID: {task.id})")
    
    def remove_task(self, task_id: int) -> bool:
        """"""
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                self._save_db()
                return True
        return False
    
    def update_task_description(self, task_id: int, description: str) -> bool:
        """"""
        for task in self._tasks:
            if task.id == task_id:
                task.description = description
                self._save_db()
                return True
        return False
    
    def update_task_status(self, task_id: int, status: TaskStatus) -> bool:
        """"""
        for task in self._tasks:
            if task.id == task_id:
                task.status = status
                self._save_db()
                return True
        return False
    
    def list_tasks(self, status: TaskStatus | None = None) -> None:
        """"""
        tasks = self._tasks.copy()
        if status:
            tasks = list(filter(lambda t: t.status == status, tasks))
        for task in tasks:
            print(f"id: {task.id} | description: {task.description} | status: {task.status}")
    
    def _save_db(self) -> None:
        """"""
        with open(self._db_path, "w") as file:
            data = [task.model_dump(mode="json") for task in self._tasks]
            json.dump(data, file, indent=4)
    
    def _generate_id(self) -> int:
        """"""
        if len(self._tasks) == 0:
            return 0
        return self._tasks[-1].id + 1
