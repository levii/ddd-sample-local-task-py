from datetime import datetime
from typing import Optional

from task.application import SheetListFetchService, SheetFetchService, SheetSaveService
from task.domain import Task, TaskName, TaskDue, TaskCollection, SheetName, Sheet


class SheetPrinter:
    def print(self, sheet):
        print(f'### Sheet:{sheet.name.value} ###')
        printer = TaskPrinter()
        for task in sheet.tasks:
            printer.print(task)
        print()


class TaskPrinter:
    def print(self, task):
        print(f'Task:{task.name.value} due={task.due.value}')


class SheetListView:
    def get(self):
        sheets = SheetListFetchService().execute()

        print(f'### Sheet 一覧 ###')
        for sheet in sheets:
            print(f'Sheet:{sheet.name.value}')

    def post(self, sheet_name: str):
        new_sheet = Sheet(
            name=SheetName(sheet_name),
            tasks=TaskCollection.build([])
        )

        sheet = SheetSaveService().execute(new_sheet)
        SheetPrinter().print(sheet)


class SheetView:
    def get(self, sheet_name: str):
        sheet = SheetFetchService().execute(SheetName(sheet_name))
        SheetPrinter().print(sheet)

    def post(self, sheet_name: str, task_name: str, task_due: Optional[str]):
        sheet = SheetFetchService().execute(SheetName(sheet_name))
        sheet.add_task(
            Task(
                name=TaskName(task_name),
                due=TaskDue(datetime.strptime(task_due, '%Y-%m-%dT%H:%M'))
            )
        )

        sheet = SheetSaveService().execute(sheet)
        SheetPrinter().print(sheet)
