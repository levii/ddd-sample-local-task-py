from task.domain import SheetCollection, Sheet, SheetName


class SheetRepository:
    def fetch_list(self) -> SheetCollection:
        raise NotImplementedError()

    def fetch(self, sheet_name: SheetName) -> Sheet:
        raise NotImplementedError()

    def save(self, sheet: Sheet) -> Sheet:
        raise NotImplementedError()
