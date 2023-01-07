import os

from rich import print
from rich.prompt import Prompt


from config import get_file_split_config, print_split_config_table
from pdf import apply_split_config

import controller

PARTITIONS_PATH = "parts"

if __name__ == "__main__":

    # controller.split_pdfs_in_directory(PARTITIONS_PATH, "dest")

    # controller.split_pdf_file(os.path.join(
    #     PARTITIONS_PATH, "Sir Duke.pdf"), "output")

    # files = os.listdir(PARTITIONS_PATH)

    # split_configs = {}

    # for file in files:
    #     file_split_config = get_file_split_config(
    #         os.path.join(PARTITIONS_PATH, file))

    #     if file_split_config:
    #         split_configs[file] = file_split_config

    # print(split_configs)

    # split_configs = {
    #     "Sir Duke.pdf": {
    #         "interval": 1,
    #         "split_vertical": True,
    #         "pages_count": 4,
    #         "prefix": "Sir Duke - "
    #     },
    #     "Oblivion.pdf": {
    #         "interval": 2,
    #         "split_vertical": False,
    #         "pages_count": 3,
    #         "prefix": "Oblivion - "
    #     },
    #     "Paris Montmartre.pdf": {
    #         # "ranges": [(1, 1), (2, 2), (3, 3)],
    #         "ranges": [(1, 1), (2, 3), (2, 2)],
    #         "split_vertical": True,
    #         "pages_count": 3,
    #         "prefix": "Paris Montmartre - "
    #     },
    # }

    config = {
        # "ranges": [(1, 1), (2, 2), (3, 3)],
        "ranges": [(1, 1), (2, 3), (2, 2), (3, 3)],
        "split_vertical": True,
        "pages_count": 2,
        "prefix": "Paris Montmartre - "
    }

    # for file, config in split_configs.items():

    #     print_split_config_table(config, file)

    #     apply_split_config(os.path.join(PARTITIONS_PATH, file),
    #                        config, destination="output")
