def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    """
    
    clean_data = []
    # iterating through values in the data list
    for value in data:
        if 'minute' in value:
            continue
        else:
            clean_data.append(float(value))

    return clean_data