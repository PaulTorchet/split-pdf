import os

from rich import print as cprint
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Confirm, Prompt, IntPrompt

from PyPDF2 import PdfReader

from util import get_filename, split_array_by_interval, split_array_by_ranges


def _get_file_size_in_mb(file_path: str, digits: int = 2) -> float:
    file_size = os.stat(file_path).st_size / (1024 * 1024)
    return round(file_size, digits)


def _format_split_ranges(ranges: str):
    formatted_ranges = []

    for curr_range in ranges.split(" "):
        if "-" in curr_range:
            formatted_ranges.append(tuple(map(int, curr_range.split("-"))))
        else:
            formatted_ranges.append((int(curr_range), int(curr_range)))

    return formatted_ranges


def _get_fake_split_result(split_config: dict):
    pages = ["Page " + str(page_index)
             for page_index in range(1, split_config["pages_count"] + 1)]

    if "interval" in split_config:
        splitted_pages = split_array_by_interval(
            pages, split_config["interval"])
    elif "ranges" in split_config:
        splitted_pages = split_array_by_ranges(pages, split_config["ranges"])
    else:
        splitted_pages = [pages]

    if split_config["split_vertical"]:
        vertically_splitted_pages = []

        for chunk in splitted_pages:
            vertically_splitted_chunks = []
            for page in chunk:
                vertically_splitted_chunks.append(page + "(L)")
                vertically_splitted_chunks.append(page + "(R)")

            vertically_splitted_pages.append(vertically_splitted_chunks)

        splitted_pages = vertically_splitted_pages

    return splitted_pages


def print_split_config_table(split_config: dict, file: str = None):

    filename = get_filename(file)

    table = Table(title=filename)
    table.add_column("Filename")
    table.add_column("Pages")

    fake_split_result = _get_fake_split_result(split_config)

    for index, chunk in enumerate(fake_split_result):
        table.add_row(split_config["prefix"].strip() + " " + str(index + 1) +
                      ".pdf", ", ".join(chunk))

    cprint(table)


def get_file_split_config(file: str, bypass_main_confirm: bool = False):

    split_config = {}

    pdf = PdfReader(file)

    split_config["pages_count"] = len(pdf.pages)

    file_size = _get_file_size_in_mb(file)

    filename = get_filename(file)

    cprint(Panel(
        f"{filename} \t {len(pdf.pages)} page(s) \t {file_size} MB"))

    if not bypass_main_confirm and not Confirm.ask("Split this file ?", default=True):
        return None

    if Confirm.ask("Split by interval ?", default=True):
        interval = IntPrompt.ask("Interval ",
                                 default=1, show_default=True)
        split_config["interval"] = interval
    else:
        ranges = Prompt.ask('Enter ranges (ex: "1-3 4 5-5 ...)" ')
        split_config["ranges"] = _format_split_ranges(ranges)

    split_config["split_vertical"] = Confirm.ask(
        "Split pages vertically ?", default=False)

    split_config["prefix"] = Prompt.ask(
        "Filename prefix ", default=f"{filename} - ")

    return split_config
