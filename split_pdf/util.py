import os


def split_array_by_interval(array: list, interval: int):
    splitted_array = []

    for i in range(0, len(array), interval):
        splitted_array.append(array[i:i+interval])

    return splitted_array


def split_array_by_ranges(array: list, ranges: list):
    splitted_array = []

    for start, end in ranges:
        sub_array = array[start - 1:end]
        if sub_array:
            splitted_array.append(sub_array)

    return splitted_array


def get_filename(file_path: str) -> str:
    return file_path.split(os.path.sep)[-1].split(".")[0]
