import dataclasses
from datetime import datetime
from typing import List, Iterator, Iterable


@dataclasses.dataclass(frozen=True)
class TaskName:
    value: str

    MIN_LENGTH = 1
    MAX_LENGTH = 30

    def __post_init__(self) -> None:
        assert (
                len(self.value) >= self.MIN_LENGTH
        ), f"TaskNameには長さ{self.MIN_LENGTH}以上の文字列を指定してください"
        assert (
                len(self.value) <= self.MAX_LENGTH
        ), f"TaskNameには長さ{self.MAX_LENGTH}以下の文字列を指定してください"


@dataclasses.dataclass(frozen=True)
class TaskDue:
    value: datetime


@dataclasses.dataclass(frozen=True)
class Task:
    name: TaskName
    due: TaskDue


@dataclasses.dataclass(frozen=True)
class TaskCollection:

    _collection: List[Task]

    def __iter__(self) -> Iterator[Task]:
        return self._collection.__iter__()

    @classmethod
    def build(cls, tasks: Iterable[Task]) -> "TaskCollection":
        return cls(list(tasks))

    def append(self, task: Task) -> "TaskCollection":
        self._collection.append(task)
        return self


@dataclasses.dataclass(frozen=True)
class SheetName:
    value: str

    MIN_LENGTH = 1
    MAX_LENGTH = 30

    def __post_init__(self) -> None:
        self.validate_filename_character()
        self.validate_length()

    def validate_filename_character(self):
        pass

    def validate_length(self):
        assert (
                len(self.value) >= self.MIN_LENGTH
        ), f"TaskNameには長さ{self.MIN_LENGTH}以上の文字列を指定してください"
        assert (
                len(self.value) <= self.MAX_LENGTH
        ), f"TaskNameには長さ{self.MAX_LENGTH}以下の文字列を指定してください"


@dataclasses.dataclass(frozen=True)
class Sheet:
    name: SheetName
    tasks: TaskCollection

    def add_task(self, task: Task):
        self.tasks.append(task)


@dataclasses.dataclass(frozen=True)
class SheetCollection:

    _collection: List[Sheet]

    def __iter__(self) -> Iterator[Sheet]:
        return self._collection.__iter__()

    @classmethod
    def build(cls, sheets: Iterable[Sheet]) -> "SheetCollection":
        return cls(list(sheets))

    def append(self, sheet: Sheet) -> "SheetCollection":
        self._collection.append(sheet)
        return self
