from task.domain import Sheet, SheetCollection, SheetName
from task.infrastructure.repository import FileSheetRepository

SHEETS_DIR = '../../../sheets'


class SheetListFetchService:
    def __init__(self):
        self._repository = FileSheetRepository(SHEETS_DIR)

    def execute(self) -> SheetCollection:
        return self._repository.fetch_list()


class SheetFetchService:
    def __init__(self):
        self._repository = FileSheetRepository(SHEETS_DIR)

    def execute(self, sheet_name: SheetName) -> Sheet:
        return self._repository.fetch(sheet_name)


class SheetSaveService:
    def __init__(self):
        self._repository = FileSheetRepository(SHEETS_DIR)

    def execute(self, sheet: Sheet) -> Sheet:
        return self._repository.save(sheet)
