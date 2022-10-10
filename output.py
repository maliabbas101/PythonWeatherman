'''
This module is used to output data.
'''
import calendar


def print_output(max_temp, min_temp, average_humidity, max_date, min_date):
    '''
    Function to print output
    '''
    max_date_array = max_date.split('-')
    min_date_array = min_date.split('-')
    max_month_name = calendar.month_name[int(max_date_array[1])]
    min_month_name = calendar.month_name[int(min_date_array[1])]
    print(
        f'Highest: {max_temp} C on {max_date_array[2]} {max_month_name}')
    print(
        f'Lowest: {min_temp} C on {min_date_array[2]} {min_month_name}')
    print(f'Average Humidity {average_humidity} %')
