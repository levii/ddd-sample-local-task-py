from datetime import datetime
from glob import glob
import json
from os.path import join, dirname, basename

from task.domain import SheetCollection, Sheet, Task, TaskCollection, TaskName, TaskDue, SheetName
from task.domain.repository import SheetRepository

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


class JSONTaskMapper:
    def serialize(self, task: Task) -> dict:
        due = None
        if task.due:
            due = datetime.strftime(task.due.value, DATETIME_FORMAT)

        return {
            'name': task.name.value,
            'due': due
        }

    def deserialize(self, j: dict) -> Task:
        due = None
        if j.get('due'):
            due = datetime.strptime(j.get('due'), DATETIME_FORMAT)

        return Task(name=TaskName(j['name']), due=TaskDue(due))


class SheetMapper:
    def serialize(self, sheet: Sheet, filepath: str):
        mapper = JSONTaskMapper()

        with open(filepath, 'w') as f:
            j = {
                'tasks': [mapper.serialize(task) for task in sheet.tasks]
            }

            json.dump(j, f, ensure_ascii=False, indent=2)

    def deserialize(self, filepath: str) -> Sheet:
        mapper = JSONTaskMapper()

        with open(filepath) as f:
            j = json.load(f)

            tasks = TaskCollection.build([])
            for taskJSON in j['tasks']:
                tasks.append(mapper.deserialize(taskJSON))

            return Sheet(name=SheetName(basename(filepath)[:-5]), tasks=tasks)


class FileSheetRepository(SheetRepository):
    def __init__(self, directory: str):
        self._directory = directory

    def fetch_list(self) -> SheetCollection:
        path = join(dirname(__file__), self._directory, '*.task')
        sheet_files = glob(path)
        mapper = SheetMapper()

        sheets = SheetCollection([])
        for sheet_file in sheet_files:
            sheets.append(mapper.deserialize(sheet_file))

        return sheets

    def fetch(self, sheet_name: SheetName) -> Sheet:
        path = join(dirname(__file__), self._directory, f'{sheet_name.value}.task')
        mapper = SheetMapper()
        return mapper.deserialize(path)

    def save(self, sheet: Sheet) -> Sheet:
        path = join(dirname(__file__), self._directory, f'{sheet.name.value}.task')
        mapper = SheetMapper()
        mapper.serialize(sheet, path)

        return sheet
