# Script used to generate an array of all files in a specified directory (included all nested files) and generates the Coverage.py command to be executed

import os

def get_file_names(path):
    arr_of_files = os.listdir(path)
    all_files = list()
    for entry in arr_of_files:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            all_files = all_files + get_file_names(full_path)
        else:
            all_files.append(full_path)
    return all_files

path = '/Users/cindy/repos/datasets-master/datasets' # TODO: change this to source code path
omit_arr = ['.DS_Store'] # TODO: update omitted array of substrings

subpath = path[:path.rfind('/')+1]
source_folder = path[path.rfind('/')+1:]

file_names_arr = get_file_names(path)
file_names_arr = list(map(lambda x: x.replace(subpath, ''), file_names_arr))

for file_name in file_names_arr:
    if [ele for ele in omit_arr if(ele in file_name)]:
        pass
    else:
        print("coverage run -a " + file_name)

print("coverage report")
print("pygount --format=summary " + source_folder)
print("pygount " + source_folder)