import os
from shutil import rmtree
from datetime import date, timedelta
from time import sleep

today = date.today().strftime('%d.%m.%Y')
last_seven_days = []
Folder_to_clear = r"C:\Printer"

# Looking for last seven days, saves it into list
for x in range(7):
    day = str(date.today() - timedelta(days=x))
    day = f"{day[-2:]}.{day[-5:-3]}.{day[0:4]}"
    last_seven_days += [day]

# Loop to search for files in chosen folder
for object in os.listdir(Folder_to_clear):

    path = os.path.join(Folder_to_clear, object)
    
    # If chosen object is not in last seven day list, and object is folder, then it will be automatically deleted
    if os.path.isdir(path):
        if object not in last_seven_days:
            print(f"Deleting {object} ...")
            print('If you wanna cancel this process press "Ctrl + C" ')
            sleep(5)
            rmtree(path)