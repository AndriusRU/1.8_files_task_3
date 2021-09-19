from pprint import pprint
import os


def all_files_in_one(list_files: list) -> None:
    result = {}
    temp_dict = {}
    for file_name in list_files:
        with open(file_name, 'r', encoding='utf-8') as file:
            count = 0
            text = []
            for line in file:
                count += 1
                text += [line.strip()]
        temp_dict[file_name] = (count, text)
    sort_keys = sorted(temp_dict, key=temp_dict.get)
    for key in sort_keys:
        result[key] = temp_dict[key]
    with open('result.txt', 'w', encoding='utf-8') as file_write:
        for f_name, value in result.items():
            file_write.write(f'{f_name}\n')
            file_write.write(f'{value[0]}\n')
            for item in value[1]:
                file_write.write(f'{item}\n')
    return


def find_files(catalog: str) -> list:
    result = []
    for file in os.listdir(catalog):
        if file.endswith('.txt'):
            result += [file]
    return result


all_files_in_one(find_files(os.getcwd()))
