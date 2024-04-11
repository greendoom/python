import os
import shutil
from datetime import datetime

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


    # Path to directory for search
search_dir = "D:/Folder"
    # Date, before searching files (year, month, day)
cutoff_date = datetime(2019, 1, 1)
    #clear file.txt
open("file.txt","w").close()


for dirpath, dirnames, filenames in os.walk(unicode(search_dir)):
    for file in filenames:
        try:
            # Get full path to file
            file_path = os.path.join(dirpath, file)
            # Get time of modification file
            creation_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # Check if date is required
            if creation_time < cutoff_date:
                #print (creation_time)
                # Write to file all found files
                with open('file.txt', 'a') as file:
                    file.write(creation_time.strftime('%d/%m/%Y') + ' ' + file_path + '\n')
                    
        except Exception as e:
            print("Error {}: {}".format(file_path, e))

print("Operation complete")