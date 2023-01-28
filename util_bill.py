import pandas as pd
import numpy as np


def read_ocr(file):
    '''read one orc file into pandas dataframe'''

    data = {"x1":[], "y1":[],"x2":[], "y2":[],"x3":[], "y3":[],"x4":[], "y4":[], "value":[]}
    with open(file) as f:
         lines = f.readlines()

         for line in lines:
            row = line.split(',', 8)

            data['x1'].append(row[0])
            data['y1'].append(row[1])
            data['x2'].append(row[2])
            data['y2'].append(row[3])
            data['x3'].append(row[4])
            data['y3'].append(row[5])
            data['x4'].append(row[6])
            data['y4'].append(row[7])
            data['value'].append(row[8])

    return pd.DataFrame(data)

def calculate_accuracy(df):
    '''
    calculate the fraction of correction prediction

    df should have a column named "document" and "prediction"
    where "prediction" is the predicted document name
    '''
    num_correct = np.sum(df["prediction"] == df["documentid"])
    return float(num_correct/len(df))
