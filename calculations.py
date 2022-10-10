from statistics import mean
import output
import dataformatting


def information(attributes, array):
    """
    Extracts information from the array.
    """
    max_array = []
    min_array = []
    humid_array = []
    date_array = []
    for item in array:
        if item[attributes.index('Max TemperatureC')] == '':
            continue
        max_array.append(int(item[attributes.index('Max TemperatureC')]))
        if item[attributes.index('Min TemperatureC')] == '':
            continue
        min_array.append(int(item[attributes.index('Min TemperatureC')]))
        if item[attributes.index(' Mean Humidity')] == '':
            continue
        humid_array.append(int(item[attributes.index(' Mean Humidity')]))
        time_standard = dataformatting.zone(attributes)
        if item[attributes.index(time_standard)] == '':
            continue
        date_array.append((item[attributes.index(time_standard)]))

    return max_array, min_array, humid_array, date_array


def calculate(max_array, min_array, humid_array, date_array):
    """
    Calculates maximum and minimum from array.
    """

    max_date, min_date = date(date_array, max_array, min_array)

    results(max(max_array), min(min_array),
            mean(humid_array), max_date, min_date)


def date(date_array, max_array, min_array):
    """
    Responsible for handling dates.
    """
    max_date = date_array[max_array.index(max(max_array))]
    min_date = date_array[min_array.index(min(min_array))]

    return max_date, min_date


def results(max_temp, min_temp, avg_humidity, max_date, min_date):
    """
    Used to display results.
    """
    output.print_output(
        max_temp, min_temp, avg_humidity, max_date, min_date)
