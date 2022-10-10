import sys
import os
from colorama import Fore
import dataformatting
import calculations
import chart


def main(argument):
    '''
    This function performs actions on base of the command line arguments.
    '''
    match argument:
        case '-e':
            files = []
            path = sys.argv[3]
            os.chdir(path)
            for file in os.listdir():
                if sys.argv[2] in file:
                    files.append(file)
            dataformatting.merge_files(files)
            attributes, array = dataformatting.read_text_file(
                'output_file.txt')
            func(attributes, array)

        case '-a':
            attributes, array = dataformatting.read_text_file(sys.argv[3])
            func(attributes, array)

        case '-c':
            attributes, array = dataformatting.read_text_file(sys.argv[3])
            max_array, min_array, humid_array, date_array = calculations.information(
                attributes, array)
            chart.bar_chart(max_array, min_array, date_array)
            chart.one_bar_chart(max_array, min_array, date_array)
        case _:
            print(Fore.RED + 'Please pass valid arguments.')


def func(attributes, array):
    """
    This is to ensure DRY code.
    """
    max_array, min_array, humid_array, date_array = calculations.information(
        attributes, array)
    calculations.calculate(max_array, min_array,
                           humid_array, date_array)


main(sys.argv[1])
