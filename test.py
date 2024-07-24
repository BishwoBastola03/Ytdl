import os
from zipfile import ZipFile

def zip_csv(directory_name, zip_file_name, filter):
   # Create object of ZipFile
   with ZipFile(zip_file_name, 'w') as zip_object:
   # Traverse all files in directory
    for folder_name, sub_folders, file_names in os.walk(directory_name):
      for filename in file_names:
      # Filter for csv files
       if filter(filename):
         # Create filepath of files in directory
         file_path = os.path.join(folder_name, filename)
         # Add files to zip file
         zip_object.write(file_path, os.path.basename(file_path))


zip_csv('./', './Zipped file.zip', lambda name: 'mp4' in name)