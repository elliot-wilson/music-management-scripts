import os

def get_subdirectories_and_files(path):    
    scan_results = os.scandir(path)
    subdirectories = []
    files = []
    for scan_result in scan_results:
        if scan_result.is_dir():
            subdirectories.append(scan_result)
        elif scan_result.is_file():
            files.append(scan_result)
    return files, subdirectories

def is_mp3(file):
    return file.name.lower().endswith("mp3")

def is_flac(file):
    return file.name.lower().endswith("flac")