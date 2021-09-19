import pandas as pd  


data = pd.read_csv('train.csv')
data_male = data[data.Sex == "male"][['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Fare']]
data_female = data[data.Sex == "female"][['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Fare']]
print("\tMALE:", data_male, sep="\n")
print("\n\tFEMALE:", data_female, sep="\n")
