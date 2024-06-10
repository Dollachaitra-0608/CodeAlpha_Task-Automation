import os
import shutil

def organize_files(source_dir, destination_dir):
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    
    files = os.listdir(source_dir)
    
    
    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):  
            file_extension = os.path.splitext(file)[1][1:]  
            if file_extension:
                
                extension_folder = os.path.join(destination_dir, file_extension.upper())  
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)
                
                
                shutil.move(os.path.join(source_dir, file), os.path.join(extension_folder, file))
                print(f"Moved {file} to {extension_folder}")


source_directory = "D:\CERTIFICATES"
destination_directory = "E:\Internship"
organize_files(source_directory, destination_directory)


