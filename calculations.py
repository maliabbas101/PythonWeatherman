from statistics import mean


def calculate(attributes, array):
    max_array = []
    min_array = []
    humid_array = []
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
    return max(max_array), min(min_array), mean(humid_array)
