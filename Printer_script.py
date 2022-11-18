import os, shutil, win32print
from time import sleep
from datetime import date

Folder_to_print = r"C:\Printer"
Current_date_folder = f"{Folder_to_print}\{date.today().strftime('%d.%m.%Y')}"

#This function read default printer, and return it.
def Default_printer():        
        printer = win32print.GetDefaultPrinter()
        return printer

# Creating folder (DD.MM.YYYY), if doesn't exist.
if os.path.exists(Current_date_folder):
        print(f"{Current_date_folder} already exist")
else:
        os.mkdir(Current_date_folder)
        
#Changing default printer to physical printer.
if Default_printer() != "Brother DCP-J105 Printer":
        win32print.SetDefaultPrinter("Brother DCP-J105 Printer")

#Loop that searches for files to print, does that, then move them to the appropriate directory.
for file in os.listdir(Folder_to_print):

        file_path = os.path.join(Folder_to_print, file)

        if os.path.isfile(file_path):
                print(f"Printing: {file}")
                os.startfile(file_path, "print")
                sleep(1)
                try:
                        shutil.move(file_path, Current_date_folder)
                
                except shutil.Error:
                        copy_number = 0
                        file_format = file[file.index("."):]
                        file_name = file[:file.index(".")]
                        old_path = file_path
                        sleep(2)
                        print(f"{file_path} already exist, changing name")

                        while os.path.exists(file_path):
                                copy_number += 1
                                file_path = f"{Current_date_folder}\{file_name} -- kopia({copy_number}){file_format}"
                                print(f"Testing {file_path} ...")
                
                try:
                        os.rename(old_path, file_path)
                        shutil.move(file_path, Current_date_folder)
                
                except shutil.Error:
                        print("shutil probably have some problems with unnecessary errors")

#Changing default printer to PDF.
if Default_printer() != "Microsoft Print to PDF":
        win32print.SetDefaultPrinter("Microsoft Print to PDF")