def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    matrix = []
    
    for x in values:
        row = []
        for power in range(degree + 1):
            row.append(x ** power)
        matrix.append(row)
    
    return matrix