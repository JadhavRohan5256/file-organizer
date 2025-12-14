from os import path, listdir, mkdir
import shutil
from logger import logger
from file_extension import all_extensions




def check_exit_in_folder(scan_path, filename):
    extension = filename.split('.')[-1]
    return path.exists(path.join(scan_path, path.join(f'{extension}_files', filename)))

def lookup(scan_path):
    print(f'🔎 scanning path : {scan_path}')
    print(f'Found unique extension files {set([filename.split('.')[-1] for filename in listdir(scan_path) if f'.{filename.split('.')[-1]}' in all_extensions])}')

    for filename in listdir(scan_path):
        extension = filename.split('.')[-1]
        if f'.{extension}' in all_extensions and check_exit_in_folder(scan_path, filename) == False:
            source = path.join(scan_path, filename)
            target = path.join(scan_path, path.join(f'{extension}_files', filename))

            if not path.exists(path.join(scan_path, f'{extension}_files')):
                mkdir(path.join(scan_path, f'{extension}_files'))
                logger.info(f'📁 folder created: {extension}_files')
            
            shutil.move(source, target)
            logger.info(f"🏃‍♀️‍➡️ file moved from '{source}' to '{target}'")
        else:
            print(f'😒 {filename} {'is the folder' if f'.{extension}' not in all_extensions else f'is file already exist inside {extension}_files folder'}.')

def scan_folder():
    response_path = input("⌨️ Enter folder path to scan : ")
    if path.exists(response_path):
        lookup(response_path.strip())
        print("🐍 File successfuly sorted according to there extensions")


if __name__ == "__main__":
    scan_folder()