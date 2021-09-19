import pandas as pd


data = pd.read_csv('train.csv')
data_name = data['Name']
dc = {}
for i in range(data_name.size):
    data_name[i] = data_name[i].split(',')[0]
    if data_name[i] not in dc:
        dc[data_name[i]] = 1
    else: dc[data_name[i]] += 1
list_dc = list(dc.items())
list_dc.sort(key=lambda i: -i[1])
print("\n10 popular name:")
for i in range(10):
    print(list_dc[i][0], '-', list_dc[i][1])
