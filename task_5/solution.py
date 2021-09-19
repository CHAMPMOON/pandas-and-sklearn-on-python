import pandas as pd


data = pd.read_csv('train.csv')
data_bool = data.isnull()
for col in data.columns:
    for i in range(data[col].size):
        if data_bool[col][i] == True:
            if i == 0:
                j = i + 1
                while True:
                    if data_bool[col][j] == False:
                        break
                    j += 1
                data[col][i] = data[col][j]
            else: 
                data[col][i] = data[col][i - 1]
print(data.isnull())
