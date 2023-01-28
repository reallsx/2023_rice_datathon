import pandas as pd;
import numpy as np;
import re;

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

            valid = False;

            value = row[8];

            # we are looking for company, address, date, amount

            v1 = '^([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/\.\-]([0-9]{0,4}) ?(([0-9][0-9])[:]([0-5][0-9]))?([:]([0-9][0-9]))? ?(PM|AM|pm|am)?$';
            v2 = '^(0?[1-9]|1[0-2])[\/](0?[1-9]|[12]\d|3[01])[\/](19|20)\d{2} ?(([0-9][0-9])[:]([0-5][0-9]))?([:]([0-9][0-9]))?$'
            v3 = '^([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/]([0-9]{0,4}) ?(([0-9][0-9])[:]([0-5][0-9]))? ?(PM|AM|pm|am)? ?([:]([0-9][0-9]))? ?(PM|AM|pm|am)?$'
            v4 = '^([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/]([0-9]{0,4}) ?(([0-9][0-9])[:]([0-5][0-9]))? ?(PM|AM|pm|am)? ?([:]([0-9][0-9]))? ?(PM|AM|pm|am)?$'
            v5 = '^([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/]([0-9]{0,4})( (([0-9][0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( (PM|AM|pm|am))?)?$';
            v6 = '^([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/\.\-]([0-9]{0,4}) ?((([0-9][0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( (PM|AM|pm|am))?)?$';
            v7 = '^(\w{0,99})[:]? ?([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/\.\-]([0-9]{0,4}) ?((([0-9][0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( (PM|AM|pm|am))?)?$';
            v8 = '^((\w{0,99})[DATE][:])? ?(([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/\.\-]([0-9]{0,4}))? ?((([0-9][0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( (PM|AM|pm|am))?)?$';
            v9 = '^((\w{0,99})[DATE|TIME] ?[:])? ?(([0-9]{0,4})[\/\.\-]([0-9]{0,2})[\/\.\-]([0-9]{0,4}))? ?((([0-9][0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( (PM|AM|pm|am))?)?$';

            # check for address
            if (len(re.findall(v9, value)) > 0):
                valid = True;

            if (valid):
                data['tl'].append(vec2(float(row[0]), float(row[1])));
                data['br'].append(vec2(float(row[4]), float(row[5])));
                data['value'].append(value);

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
