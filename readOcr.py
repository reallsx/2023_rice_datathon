import pandas as pd;
import pathlib;
import os;

root = pathlib.Path(__file__).parent.resolve();
root = f"{root}/ocr";

filesList = os.listdir(root);

dfDict = dict();

for i in range(len(filesList)):
    fileName = filesList[i];
    path = f"{root}/{fileName}";

    data = {"x1":[], "y1":[],"x2":[], "y2":[],"x3":[], "y3":[],"x4":[], "y4":[], "value":[]};

    with open(path) as file:
        lines = file.readlines();

        print(path);

        for line in lines:
            row = line.split(',', 8);

            data['x1'].append(row[0]);
            data['y1'].append(row[1]);
            data['x2'].append(row[2]);
            data['y2'].append(row[3]);
            data['x3'].append(row[4]);
            data['y3'].append(row[5]);
            data['x4'].append(row[6]);
            data['y4'].append(row[7]);
            data['value'].append(row[8]);

        file.close();

    dfDict[fileName.split('.')[0]] = pd.DataFrame(data);



'''
# pandas data frame
users = pd.read_csv("Users.csv");

numRows = len(users.index);
numCols = len(users.columns);

#documentid    paymentid    amount    date    vendor_name    vendor_address
class receipt:
    document_id = "";
    payment_id ="";
    amount = 0;
    date = "";
    vendor_name = "";
    vendor_address = "";
    def __init__(self):
        self.document_id;
        self.payment_id;
        self.amount;
        self.date;
        self.vendor_name;
        self.vendor_address;

class vec2:
    x = 0;
    y = 0;
    def __init__(self, _x, _y):
        self.x = _x;
        self.y = _y;

class textBox:
    pos = vec2(0,0);
    dim = vec2(0,0);
    text = "";
    def __init__(self, _x, _y, _w, _h, _text):
        self.pos = vec2(_x, _y);
        self.dim = vec2(_w, _h);
        self.text = _text;

# get all receipt data
receiptData = [];
for r in range(numRows):
    nr = receipt();

    nr.document_id    = users.iat[r, 0];
    nr.payment_id     = users.iat[r, 1];
    nr.amount         = users.iat[r, 2];
    nr.data           = users.iat[r, 3];
    nr.vendor_name    = users.iat[r, 4];
    nr.vendor_address = users.iat[r, 5];

    receiptData.append(nr);


# get all text data
textBoxes = [];

numReceipts = len(receiptData);
for r in range(numReceipts):
    documentPath = f"odr/{receiptData[r].document_id}.csv";

    receiptFile = np.read_csv(path);

    numRows = len(receiptFile.index);
    numCols = len(receiptFile.columns);

    for r in range(numRows):

        tBox = textBox;

        x1 = receiptFile.iat[r, 0];
        y1 = receiptFile.iat[r, 1];

        x3 = receiptFile.iat[r, 4];
        y3 = receiptFile.iat[r, 5];

        w = x3 - x1;
        h = y3 - y1;

        tBox.pos = vec2(x1, y1);
        tBox.dim = vec2(w, h);
        tBox.text = receiptFile.iat[r, 8];

        textBoxes.append(tBox);



# compare a row
'''



