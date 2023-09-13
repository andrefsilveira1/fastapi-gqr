def find_best_gqr(arr, limit=None):
    result = []
    
    for data in arr:
        depth = float(data['depth'])
        gqr = calculate_gqr(data)
        result.append({'depth': depth, 'gqr': gqr})
    
    result.sort(key=lambda x: x['gqr'])
    
    if limit:
        greatest = result[-10:]
    else:
        greatest = result
    
    average = calculate_average_values(greatest)
    deviation = calculate_deviation(greatest)

    return {'greatest': greatest, 'average': average, 'deviation': deviation}
