from pydantic import BaseModel, Field
from enum import StrEnum
from datetime import datetime


class TaskStatus(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


class Task(BaseModel):
    id: int
    description: str
    status: TaskStatus = Field(default=TaskStatus.TODO)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def update(self) -> None:
        """"""
        self.updated_at = datetime.now()
