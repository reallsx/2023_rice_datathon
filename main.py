import pandas as pd;
import pathlib;
import os;
import fuzzywuzzy as fw;

from util_bill import *

# other stuff

data = readUserFile();

userData = data[0];
testData = data[1];

# get the data from all of
root = pathlib.Path(__file__).parent.resolve();
root = f"{root}/ocr";

filesList = os.listdir(root);

dfDict = dict();

count = 0;

for i in range(len(filesList)):
    fileName = filesList[i];
    path = f"{root}/{fileName}";

    df = read_ocr(path);
    count += (len(df.index));
    #print(fileName);
    #print(df);

    dfDict[fileName.split('.')[0]] = df;

# now go through the user dataset and determine which one is best
numRows = userData.shape[0];
numCols = userData.shape[1];

for r in range(numRows):
    # for each entry in userdata

    row = userData[r, :];

    #amount,date,vendor_name,vendor_address
    amount = row[0];
    date = row[1];
    vendor_name = row[2];
    vendoor_address = row[3];

    matchingFile = "";

    # insert algorithm to match these values to each file and to each row













