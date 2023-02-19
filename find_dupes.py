import os
import sys

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

def contains_both_mp3_and_FLAC(file_array):
    mp3_count = 0
    FLAC_count = 0

    for file in file_array:
        if file.name.lower().endswith("mp3"):
            mp3_count += 1
        elif file.name.lower().endswith("flac"):
            FLAC_count += 1
        
        if mp3_count and FLAC_count:
            return True
    
    return False

def recursively_search_subdirectories_for_mixed_music_files(path):
    files, subdirectories = get_subdirectories_and_files(path)
    if len(files) and contains_both_mp3_and_FLAC(files):
        print(path)
    if len(subdirectories):
        for subdirectory in subdirectories:
            recursively_search_subdirectories_for_mixed_music_files(subdirectory.path)

recursively_search_subdirectories_for_mixed_music_files(directory_path)

