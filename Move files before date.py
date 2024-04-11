# -*- coding: utf-8 -*-
import os
import shutil
from datetime import datetime

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


    # Path to directory for search
search_dir = "D:/Folder"
    # Path to directory for transfer
dest_dir = "D:/Folder2"
    # Date, before searching files (year, month, day)
cutoff_date = datetime(2019, 1, 1)

for dirpath, dirnames, filenames in os.walk(unicode(search_dir)):
    for file in filenames:
        try:
            # Get full path to file
            file_path = os.path.join(dirpath, file)
            # Get time of modification file
            creation_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # Check if date is required
            if creation_time < cutoff_date:
                # Create path in destination folder, saving structure
                dest_path = os.path.join(dest_dir, os.path.relpath(dirpath, search_dir))
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                    # Move file
                shutil.move(file_path, os.path.join(dest_path, file))
        except Exception as e:
            print("Error during transfer {}: {}".format(file_path, e))

print("Transfer files complete")