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
    print(df);

    dfDict[fileName.split('.')[0]] = df;


print(count / 562.0);



