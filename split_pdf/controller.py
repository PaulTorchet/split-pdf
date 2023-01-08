import os

from rich.prompt import Confirm

from split_pdf.config import get_file_split_config, print_split_config_table
from split_pdf.pdf import apply_split_config


def split_pdfs_in_directory(source: str, destination: str):
    files = [file for file in os.listdir(
        source) if file.lower().endswith('.pdf')]

    split_configs = {}

    for file in files:
        file_split_config = get_file_split_config(
            os.path.join(source, file))

        if file_split_config:
            split_configs[file] = file_split_config

    for file, config in split_configs.items():
        print_split_config_table(config, file)

    if not Confirm.ask(f"Create these files in '{os.path.abspath(destination)}' ?", default=True):
        return

    for file, config in split_configs.items():
        apply_split_config(os.path.join(source, file),
                           config, destination)


def split_pdf_file(file: str, destination: str):
    file_split_config = get_file_split_config(file, bypass_main_confirm=True)

    if not file_split_config:
        return

    print_split_config_table(file_split_config, file)

    if not Confirm.ask(f"Create these files in '{os.path.abspath(destination)}' ?", default=True):
        return

    apply_split_config(file, file_split_config, destination)
