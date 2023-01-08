# Split-PDF CLI

This CLI allows to separate PDF files, by pages, or vertically in the pages.

You can split pages by :

- interval : split pdf every `n` pages
- ranges : choose the ranges manually (`1-2 3-4`, ...)

This tool is mainly used for sheet music, but can also be used for all types of PDF.

> This is a first version, many bugs can occure...

## Features

- Split a specific PDF file (`file` command)
- Split all PDFs in a directory (`directory` or `dir` command)

All sub-files will be writed in a subfolder with the name of the original file. (Ex : the sub-files of `BigFile.pdf` will be written in `BigFile/*` next to the original file.)

For each file, you will be asked:

1. Split this file ? (only if in `dir` mode)
2. Split by interval ?
   - If yes, the interval (`int`)
   - Else, the range (Ex : `1-2 3-4`, `1 2 3-4 5-5`, `2 3-5 1-4 3`, ...)
3. Split the pages vertically ? (50/50 ratio, when 2 pages are on the same PDF page)
4. The prefix for created files

## Commands

- Split a specific PDF file :

```bash
split-pdf file path/to/file.pdf
```

- Split all PDFs in a directory :

```bash
split-pdf directory path/to/pdfs/
# OR
split-pdf dir path/to/pdfs/
```
