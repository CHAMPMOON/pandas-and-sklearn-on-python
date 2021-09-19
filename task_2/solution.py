import pandas as pd  


data = pd.read_csv('train.csv')
data_male = data[data.Sex == "male"][['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Fare']]
data_female = data[data.Sex == "female"][['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Fare']]
print(data_male, data_female, sep="\n")
