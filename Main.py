import os
from shutil import move
from time import sleep
from datetime import date

Folder_to_print = r"C:\Printer"
Current_date_folder = f"{Folder_to_print}\{date.today().strftime('%d.%m.%Y')}"

# Creating folder (DD.MM.YYYY)
try:
        os.mkdir(Current_date_folder)
except Exception:
        print(f"{Current_date_folder} already exist")


# Loop to search for files to print, doing it and then moving them to correct directory
for file in os.listdir(Folder_to_print):

        file_path = os.path.join(Folder_to_print, file)

        if os.path.isfile(file_path):
                print(f"Printing {file}")
                os.startfile(file_path, "print")        
                sleep(8)
                move(file_path, Current_date_folder)
