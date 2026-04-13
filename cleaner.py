def clean_data(data):
    """
    Description: 
        Cleaning the provided dataset of user viewing times.
        Removing the header row/values.
        Ensuring that all values are of numerical float dtype.

    Input:
        data: list of strings representing user viewing times

    Output:
        clean_data: list of float values representing user viewing times.

    """
    
    clean_data = []
    # iterating through values in the data list
    for value in data:
        # removing data header
        if 'minute' in value:
            continue
        else:
            # typecasting to numerical format
            clean_data.append(float(value))

    return clean_data