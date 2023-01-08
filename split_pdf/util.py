import os


def split_array_by_interval(array: list, interval: int) -> list[list]:
    """Split an array by interval.

    Args:
        array (list): Array to split.
        interval (int): Size of the chunks.

    Returns:
        list[list]: List of splitted chunks.
    """
    splitted_array = []

    for i in range(0, len(array), interval):
        splitted_array.append(array[i:i+interval])

    return splitted_array


def split_array_by_ranges(array: list, ranges: list[tuple]) -> list[list]:
    """Split an array by ranges.

    Args:
        array (list): List to split.
        ranges (list[tuple]): Ranges as list of tuples (end, start).

    Returns:
        list[list]: List of splitted chunks.
    """
    splitted_array = []

    for start, end in ranges:
        sub_array = array[start - 1:end]
        if sub_array:
            splitted_array.append(sub_array)

    return splitted_array


def get_filename(file_path: str) -> str:
    """Get file name without path nor extension.

    Args:
        file_path (str): File path.

    Returns:
        str: File name.
    """
    return file_path.split(os.path.sep)[-1].split(".")[0]
