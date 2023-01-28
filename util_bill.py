def calculate_accuracy(df):
    '''
    calculate the fraction of correction prediction

    df should have a column named "document" and "prediction"
    where "prediction" is the predicted document name
    '''
    num_correct = np.sum(df["prediction"] == df["documentid"])
    return float(num_correct/len(df))