# Printer_extension
  Printer_script will:
1. Create directory(DD/MM/YYYY),
2. Set Default printer as physical printer,
3. From chosen folder:
    * Print file 
    * Move file to previously created folder, if some file have the same path:
        - Add and changing suffix of current file as long as needed
        - Finally move file with changed name to folder
4. Set Defualt printer as PDF printer

  Folder_organizer will:
1. Create list of last seven days,
2. Check chosen folder:
    * If object is dictionary, and last seven days list doesn't include it:
        - Show you message and give you time to cancel this process,
        - If you don't do it then the folder will be removed