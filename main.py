import sys
import os
# import calendar
import dataformatting
import calculations
import output


def number_to_string(argument):
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

            # array_date, array_temp = yearly.read_text_file(
            #     file)
            # yearly.calculate_max(array_date, array_temp)
            return "Yearly"
        case '-a':
            # current_month_name = calendar.month_name[int(
            # sys.argv[2].split('/')[1])]
            attributes, array = dataformatting.read_text_file(sys.argv[3])
            max_temp, min_temp, avg_humidity = calculations.calculate(
                attributes, array)
            output.printing_monthly_data(
                max_temp, min_temp, avg_humidity)
            return "Monthly"
        case '-c':
            return "Chart"
        case _:

            return "Not a valid argument passed."


print(number_to_string(sys.argv[1]))
