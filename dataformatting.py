

# def read_text_file(file_path):
#     arrayDate, arrayTemp = [], []
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#         print(lines)
#         for line in range(1, len(lines)):
#             array = (lines[line].split(','))
#             if array[1] == '':
#                 continue
#             arrayDate.append(array[0])
#             arrayTemp.append(int(array[1]))
#     return arrayTemp

def read_text_file(file_path):

    array = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        attributes = lines[0].split(',')
        for line in range(1, len(lines)):
            array.append((lines[line].split(',')))
    return attributes, array


def merge_files(files):

    with open("output_file.txt", "w") as outfile:
        for filename in files:
            with open(filename) as infile:
                contents = infile.read()
                outfile.write(contents)
