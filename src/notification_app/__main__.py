import time

from task.application import SheetListFetchService

if __name__ == '__main__':
    print('Start Notification App')

    while True:
        print('Fetch and check tasks...')
        sheets = SheetListFetchService().execute()
        time.sleep(10)
