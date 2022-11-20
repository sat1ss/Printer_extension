#pywintypes is extremely important if you wanna convert this into .exe
import os, shutil, pywintypes           
from win32.win32print import *
from time import sleep
from datetime import date

Folder_to_print = r"C:\Printer"
Current_date_folder = f"{Folder_to_print}\{date.today().strftime('%d.%m.%Y')}"

#This function read default printer, and return it.
def Default_printer():        
        printer = GetDefaultPrinter()
        return printer

# Creating folder (DD.MM.YYYY), if doesn't exist.
if os.path.exists(Current_date_folder):
        print(f"{Current_date_folder} already exist")
else:
        os.mkdir(Current_date_folder)
        
#Changing default printer to physical printer.
if Default_printer() != "Brother DCP-J105 Printer":
        SetDefaultPrinter("Brother DCP-J105 Printer")
print("-----------------------------------------------------------------------------")

#Loop that searches for files to print, does that, then move them to the appropriate directory.
for file in os.listdir(Folder_to_print):

        file_path = os.path.join(Folder_to_print, file)

        if os.path.isfile(file_path):
                print(f"Printing: {file}")
                os.startfile(file_path, "print")
                sleep(8)
                try:
                        shutil.move(file_path, Current_date_folder)
                #Expect that some file can already have the same name
                except shutil.Error:
                        number_of_copy = 0
                        file_format = file[file.index("."):]
                        file_name = file[:file.index(".")]
                        old_path = file_path
                        print(f"{file_path} already exist, changing name")
                
                #New name is Current name+" -- copy(number_of_copy)" 
                        while os.path.exists(file_path):
                                number_of_copy += 1
                                file_path = f"{Current_date_folder}\{file_name} -- copy({number_of_copy}){file_format}"
                
                #Rename file and expect some bug I think with shutil
                try:
                        os.rename(old_path, file_path)
                        print(f'Name changed sucessfully to: "{file_name} -- copy({number_of_copy}){file_format}"')
                        shutil.move(file_path, Current_date_folder)
                except shutil.Error:
                        print("Shutil probably have some problems with unnecessary errors")
                print("-----------------------------------------------------------------------------")               

#Changing default printer to PDF.
if Default_printer() != "Microsoft Print to PDF":
        SetDefaultPrinter("Microsoft Print to PDF")
        print("Printer changed to: \"Microsoft Print to PDF\"")
sleep(10)