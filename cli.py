import os

import click
from click_aliases import ClickAliasedGroup

from controller import split_pdfs_in_directory, split_pdf_file

# for specific file
# with options

# for directory


@click.group(cls=ClickAliasedGroup)
def cli():
    """Split PDF file(s) by pages and/or vertically."""
    pass


@cli.command()
@click.argument("source", type=click.Path(exists=True, dir_okay=False))
@click.option("-d", "--destination", default=None, type=click.Path(exists=True, file_okay=False), help="Directory where to write PDF files.")
def file(source, destination):
    """Split a specific PDF file."""
    if not destination:
        destination = os.path.dirname(source)

    split_pdf_file(source, destination)


@cli.command(aliases=["dir"])
@click.argument("source", default=".", type=click.Path(exists=True, file_okay=False))
@click.option("-d", "--destination", default=None, type=click.Path(exists=True, file_okay=False), help="Directory where to write PDF files.")
def directory(source, destination):
    """Split all PDF files in directory."""
    if not destination:
        destination = source

    split_pdfs_in_directory(source, destination)


if __name__ == "__main__":
    cli()
