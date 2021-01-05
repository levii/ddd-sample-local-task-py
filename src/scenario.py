from task_app.presentation import SheetListView, SheetView

print('-'*10)
print(f'> Sheet 一覧を表示')
print()
SheetListView().get()
print()

target_sheet_name = 'my'
print('-'*10)
print(f'> Sheet {target_sheet_name} を表示')
print()
SheetView().get(target_sheet_name)
print()


target_sheet_name = 'new'
print('-'*10)
print(f'> Sheet {target_sheet_name} を作成')
print()
SheetListView().post(target_sheet_name)
print()


print('-'*10)
print(f'> Task を {target_sheet_name} に追加')
print()
SheetView().post(target_sheet_name, '新しいタスク', '2021-01-06T10:00')
print()

print('-'*10)
print(f'> Sheet 一覧を表示')
print()
SheetListView().get()
print()
