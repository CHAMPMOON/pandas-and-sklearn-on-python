import pandas as pd


data = pd.read_csv('train.csv')
data = data[['Embarked', 'Survived']]

data_s = data[data.Embarked == 'S'][['Survived']]
data_s = data_s.groupby(['Survived'])['Survived'].count()
data_s.name = "Survived from port S"
print(data_s, "\n")

data_c = data[data.Embarked == 'C'][['Survived']]
data_c = data_c.groupby(['Survived'])['Survived'].count()
data_c.name = "Survived from port C"
print(data_c, "\n")

data_q = data[data.Embarked == 'Q'][['Survived']]
data_q = data_q.groupby(['Survived'])['Survived'].count()
data_q.name = "Survived from port Q"
print(data_q, "\n")

# Во всех портах есть как выжившие, так и нет. Однако посчитаем процент выживаемости:
# Для порта S:   33.7%
# Для порта С:   55.4%
# Для порта Q:   39%
# Делаем вывод, что порт влияет на выживаемость. Самый безопасный порт - С
