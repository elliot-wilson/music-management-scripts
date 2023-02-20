import mutagen
import os
import sys

from datetime import timedelta

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

def stringify_length(seconds):
    nonpadded_string = str(timedelta(seconds=seconds))
    split_string = nonpadded_string.split(":")
    split_string[0] = split_string[0].zfill(2)
    split_string[2] = split_string[2][:2]
    joined_string = ":".join(split_string)
    return joined_string
    

def calculate_length(audio_files):
    length_in_secs = 0
    for audio_file in audio_files:
        length_in_secs += audio_file.info.length
    return stringify_length(length_in_secs)


def write_albumlength_tag(files):
    audio_files = [mutagen.File(file.path) for file in files if mutagen.File(file.path)]
    length = calculate_length(audio_files)
    print(length)


def recursively_search_subdirectories(path):
    print(path)
    files, subdirectories = get_subdirectories_and_files(path)
    if len(files):
        write_albumlength_tag(files)
    if len(subdirectories):
        for subdirectory in subdirectories:
            recursively_search_subdirectories(subdirectory.path)

def main():
    recursively_search_subdirectories(directory_path)

if __name__ == "__main__":
    main()