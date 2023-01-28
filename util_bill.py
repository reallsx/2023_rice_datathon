import pandas as pd;
import numpy as np;
import re;
import dateutil.parser as dparser;

# read a single csv file
# store data from csv file in a panda dataframe
# each row is vec2 topleft, vec2 bottomright, value
def read_ocr(file):
    '''read one orc file into pandas dataframe'''

    data = {"tl":[], "br":[], "value":[]};

    with open(file) as f:
         lines = f.readlines()

         counter = 0;

         for line in lines:
            row = line.split(',', 8)

            valid = False;

            value = row[8];

            # we are looking for company, address, date, amount

            # check for date

            #v14 = '^((DATE|DATE )?[:])? ?(?![\-])(([0-9]{0,4})[\/\.\- ]([0-9]{0,2}|[\w]{1,})[\/\.\- ]([0-9]{0,4})) ?((([0-9]?[0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( ?[\w ]{1,})?)?$';

            #v15 = '^([\w\-\.\# \:]{0,}|(DATE|DATE )?[:])? ?(?![\-])(([0-9]{1,4})[\/\.\- ]([0-9]{1,2}|[\D]{1,})[\/\.\- ]([0-9]{1,4})) ?((([0-9]?[0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( ?(PM|AM|pm|am)|[\w ]{0,}?))?$'

            #v16 = '^([\D\#\- ]{0,}|(DATE|DATE )?[:])? ?(?![\-])(([0-9]{1,4})[\/\.\- ]([0-9]{1,2}|([\D^ ^\-][]{1,}))[\/\.\- ]([0-9]{1,2})|([0-9]{1,2})[\/\.\- ]([0-9]{1,2}|[\D]{1,})[\/\.\- ]([0-9]{1,4})) ?((([0-9]?[0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( ?(PM|AM|pm|am)|[\w ]{0,}?))?$';

            dateCheck = '(?![\-])(([0-9]{1,4})[\/\.\- ]([0-9]{1,2}|([\D^ ^\-]{1,}))[\/\.\- ]([0-9]{1,4}))( (([0-9]?[0-9])[:]([0-9][0-9]))([:]([0-9][0-9]))?( ?(PM|AM|pm|am)))?';

            if (len(re.findall(dateCheck, value)) > 0):
                valid = True;

            # check for number
            numberMatch = '[-]?[\d]{1,}[.]{1}[\d]{1,}';

            if (len(re.findall(numberMatch, value)) > 0):
                valid = True;

            # company and address, should be in first few rows
            if (counter < 5):
                counter += 1;
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

    return float(num_correct/len(df));

# structure for storing a 2d point
class vec2:
    x = 0;
    y = 0;
    def __init__(self, _x, _y):
        self.x = _x;
        self.y = _y;
