import os
import shutil
import datetime

source_directory = "C:\\Users\\User\\Desktop\\source_directory"
destination_directory = "C:\\Users\\User\\Desktop\\destination_directory"

current_date = datetime.datetime.now().strftime("%Y%m%d")

for filename in os.listdir(source_directory):
    if filename.endswith(".logs"):
        parts = filename.split("_logs_")
        if len(parts) == 2:
            application_name, creation_date = parts
            new_filename = f"archive_{application_name}_logs_{current_date}.logs"
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, new_filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {new_filename}")

print("Log file renaming and moving complete.")
