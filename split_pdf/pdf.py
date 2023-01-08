import os
from copy import copy

from PyPDF2 import PdfReader, PdfWriter, PageObject

from split_pdf.util import get_filename, split_array_by_interval, split_array_by_ranges

ANGLES = {
    270: {"left": ("bottom", "top"), "right": ("top", "top")},
    0: {"left": ("right", "right"), "right": ("left", "right")}
}


def trim_page_left(page: PageObject) -> PageObject:
    """Get left side of a page.

    Args:
        page (PageObject): Page.

    Returns:
        PageObject: Left side of the page.
    """
    start, end = ANGLES[page.rotation]["left"]

    setattr(page.cropbox, start, getattr(page.cropbox, end) / 2)

    return page


def trim_page_right(page: PageObject) -> PageObject:
    """Get right side of a page.

    Args:
        page (PageObject): Page.

    Returns:
        PageObject: Right side of the page.
    """
    start, end = ANGLES[page.rotation]["right"]

    setattr(page.cropbox, start, getattr(page.cropbox, end) / 2)

    return page


def split_page_vertically(page: PageObject) -> tuple[PageObject, PageObject]:
    """Split page and return both sides as single pages.

    Args:
        page (PageObject): Page to split vertically.

    Returns:
        tuple[PageObject, PageObject]: Left and right pages.
    """
    left_page = trim_page_left(copy(page))
    right_page = trim_page_right(copy(page))

    return (left_page, right_page)


def split_chunk_pages_vertically(chunk: list[PageObject]) -> list[PageObject]:
    """Split vertically each page of the list.

    Args:
        chunk (list[PageObject]): List of pages.

    Returns:
        list[PageObject]: List of pages splitted vertically.
    """
    splitted_chunk = []

    for page in chunk:
        left, right = split_page_vertically(page)

        splitted_chunk.append(left)
        splitted_chunk.append(right)

    return splitted_chunk


def split_chunks_vertically(pdf_chunks: list) -> list[list]:
    """Split each page of each chunk in list.

    Args:
        pdf_chunks (list): List of chunks (list of pages).

    Returns:
        list[list]: List of chunks whose pages have been splitted vertically.
    """
    splitted_chunks = []

    for chunk in pdf_chunks:
        splitted_chunks.append(split_chunk_pages_vertically(chunk))

    return splitted_chunks


def write_pdf_chunks(pdf_chunks: list, destination: str, prefix: str):
    """Write PDF files for each chunk in directory

    Args:
        pdf_chunks (list): List of chunks (list of pages).
        destination (str): Destination directory.
        prefix (str): Prefix of each created files.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)

    for index, chunk in enumerate(pdf_chunks):
        writer = PdfWriter()

        for page in chunk:
            writer.add_page(page)

        with open(os.path.join(destination, prefix.strip() + " " + str(index + 1) + ".pdf"), "wb") as output_pdf:
            writer.write(output_pdf)


def apply_split_config(file: str, config: dict, destination: str = ""):
    """Apply split configuration to a PDF file.

    Args:
        file (str): File path.
        config (dict): Split configuration
        destination (str, optional): Directory where to create sub-folder for splitted files. Defaults to "".
    """
    filename = get_filename(file)

    pdf = PdfReader(file)

    if "interval" in config:
        pdf_chunks = split_array_by_interval(pdf.pages, config["interval"])

    elif "ranges" in config:
        pdf_chunks = split_array_by_ranges(pdf.pages, config["ranges"])

    else:
        pdf_chunks = [pdf.pages]

    if config["split_vertical"]:
        pdf_chunks = split_chunks_vertically(pdf_chunks)

    write_pdf_chunks(pdf_chunks, os.path.join(
        destination, filename), config["prefix"])
