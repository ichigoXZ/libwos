import pandas as pd

cfile = "C1-final.csv"
tfile = "C1-final.txt"
data = pd.read_csv(cfile)

with open(tfile, 'w') as f:
    for line in data.values:
        for i, val in enumerate(line):
            if i == 0:
                s = str(val)
            else:
                if str(val) == "nan":
                    s = s + "###" + "null"
                else:
                    s = s + '###' + str(val)
        f.writelines(s+'\n')
