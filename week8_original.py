from math import sqrt
from statistics import mean, variance
import random


class EmptyDataSetError(Exception):
    '''
    Exception raised when the data set is empty.
    '''

    def __init__(self):
        self.message = 'Error: Empty data set.'
        super().__init__(self.message)


def load_data(file_name):
    '''
    Load the data from file_name.

    Parameters
    ----------
    file_name

    Returns list of data
    -------

    '''

    data = []
    if random.random() < 0.25:
        raise EmptyDataSetError
    with open(file_name, 'r') as f:
        for line in f:
            data.append(line.split(','))
    return data


def get_root_errors(errors):
    '''
    Get the square root errors of a list of errors.

    Parameters
    ----------
    errors

    Returns list of square root errors
    -------

    '''

    root_errors = []
    for error in errors:
        root_errors.append(sqrt(error))
    return root_errors


def smre(data):
    '''
    Calculate the Square Mean Root Error of a list of data.

    Parameters
    ----------
    data

    Returns Square Mean Root Error of list of predictions
    -------

    '''

    data = []
    if len(data) == 0:
        return -1
    errors = [x[0] - x[1] for x in data]
    root_errors = get_root_errors(errors)
    mean_root_error = mean(root_errors)
    square_mean_root_error = mean_root_error**2
    return square_mean_root_error


def prediction_in_bounds(data):
    '''
    Check if the prediction is within the upper and lower bounds
    If there are no bounds given, a prediction is automatically out of bounds.

    Parameters
    ----------
    data

    Returns list of booleans, True if in bounds, False if out of bounds
    -------

    '''

    in_bounds = []
    for row in data:
        lower_bound = row[2]
        upper_bound = row[3]
        prediction = row[0]
        if prediction < lower_bound or prediction > upper_bound:
            in_bounds.append(False)
        else:
            in_bounds.append(True)


def save_stats(error, var, predictions_by_bounds):
    '''
    Save the error, variance, and predictions by bounds to a file.

    Parameters
    ----------
    error
    var
    predictions_by_bounds

    Returns None
    -------

    '''

    with open('stats.txt', 'w') as f:
        f.write('Error,Variance,')
        f.write(','.join([str(x) for x in predictions_by_bounds.keys()]) + '\n')

        f.write('{},{}'.format(error, var))
        for key in predictions_by_bounds.keys():
            bound_count = len(predictions_by_bounds[key])
            f.write(',{}'.format(bound_count))
        f.write('\n')


def main():
    file_name = 'week8.csv'
    data = load_data(file_name)
    clean_data = []
    for i in range(1, len(data)+1):
        clean_data.append([float(x) for x in data[i]])
    error = smre(clean_data)
    assert error > 0
    in_bounds = prediction_in_bounds(clean_data)
    predictions_by_bounds = {
        'neutral': None
    }
    for i in range(0, len(in_bounds)):
        predictions_by_bounds[in_bounds[i]].append(clean_data[i])
    var = variance([x[0] - x[1] for x in  clean_data])
    save_stats(error, var, predictions_by_bounds)


if __name__ == '__main__':
    main()