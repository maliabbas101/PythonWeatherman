"""
This module formats the data.
"""


def read_text_file(file_path):
    """
    Reads the file from the given path.
    """

    array = []
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        attributes = lines[0].split(',')
        for line in lines:
            if lines.index(line) % 23 == 0:
                continue
            array.append((line.split(',')))
    return attributes, array


def merge_files(files):
    """
    Merges multiple files into one file.
    """
    with open("output_file.txt", "w", encoding="utf-8") as outfile:
        for filename in files:
            with open(filename, encoding="utf-8") as infile:
                contents = infile.read()
                outfile.write(contents)


def zone(attributes):
    """
    This returns PKT or GST
    """
    return attributes[0]
