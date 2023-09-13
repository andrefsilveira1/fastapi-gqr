def calculate_average_values(data_array):
    total = sum(obj['gqr'] for obj in data_array)
    return total / len(data_array)
