import os
import sys

from utils import is_flac, is_mp3

directory_path = sys.argv[1]

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

def contains_both_mp3_and_FLAC(files):
    mp3_count = 0
    flac_count = 0

    for file in files:
        if is_mp3(file):
            mp3_count += 1
        elif is_flac(file):
            flac_count += 1
        
        if mp3_count and flac_count:
            return True
    
    return False

def find_mp3s(files):
    mp3s = []
    for file in files:
        if is_mp3(file):
            mp3s.append(file)
    return mp3s

def prompt_delete_dupes(path, files):
    sorted_files = sorted(files, key=lambda file: is_flac(file))
    for file in sorted_files:
        print(file.name)
    response = input("Delete? y/n: ")
    if response.lower() == "y":
        for file in find_mp3s(files):
            os.remove(file.path)
        print("Successfully deleted")

    else:
        pass # replace with writing path to log file, probably by refactoring this into a class?
    print("")


def recursively_search_subdirectories_for_mixed_music_files(path):
    print(path)
    files, subdirectories = get_subdirectories_and_files(path)
    if len(files) and contains_both_mp3_and_FLAC(files):
        prompt_delete_dupes(path, files)
    if len(subdirectories):
        for subdirectory in subdirectories:
            recursively_search_subdirectories_for_mixed_music_files(subdirectory.path)

recursively_search_subdirectories_for_mixed_music_files(directory_path)

