from shutil import copytree, copyfile
import os

base_dir = "audio"
for filename in os.listdir(base_dir):
    new_filename = filename.strip()
    print(f"'{filename}' -> '{new_filename}'")
    copyfile(f"{base_dir}/{filename}", f"{base_dir}_renamed/{new_filename}")