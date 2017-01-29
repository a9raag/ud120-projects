#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

            Return a list of tuples named cleaned_data where
            each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = [(ages[i], net_worths[i], abs(predictions[i] - net_worths[i])) for i in range(len(predictions))]
    fraction = int(len(predictions) * 0.9)
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])




    return cleaned_data[:fraction]
