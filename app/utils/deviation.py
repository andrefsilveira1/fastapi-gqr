import math

def calculate_deviation(data_array):
    if len(data_array) <= 1:
        return 0

    media = calculate_average_values(data_array)
    squared_differences = [(obj['gqr'] or 0 - media) ** 2 for obj in data_array]
    variance = sum(squared_differences) / (len(data_array) - 1)
    standard_deviation = math.sqrt(variance)
    return standard_deviation
