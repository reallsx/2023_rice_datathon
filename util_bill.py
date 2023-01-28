import pandas as pd
import numpy as np

# read a single csv file
# store data from csv file in a panda dataframe
# each row is vec2 topleft, vec2 bottomright, value
def read_ocr(file):
    '''read one orc file into pandas dataframe'''

    data = {"tl":[], "br":[], "value":[]};

    with open(file) as f:
         lines = f.readlines()

         for line in lines:
            row = line.split(',', 8)

            data['tl'].append(vec2(float(row[0]), float(row[1])));
            data['br'].append(vec2(float(row[4]), float(row[5])));
            data['value'].append(row[8]);

    return pd.DataFrame(data)

# read the User.csv file
# @return: a tuple of two dataframes, the first being the test data
# and the second being the actual data
def readUserFile():

    users_csv = pd.read_csv(f"./Users.csv");
    user_data = users_csv.iloc[:, -4:];
    test_data = users_csv.iloc[:, :2];

    return user_data, test_data;

# calculate accuracy
# return float [0, 1]
def calculate_accuracy(df):
    '''
    calculate the fraction of correction prediction

    df should have a column named "document" and "prediction"
    where "prediction" is the predicted document name
    '''
    num_correct = np.sum(df["prediction"] == df["documentid"])

    return float(num_correct/len(df))



# structure for storing a 2d point
class vec2:
    x = 0;
    y = 0;
    def __init__(self, _x, _y):
        self.x = _x;
        self.y = _y;
