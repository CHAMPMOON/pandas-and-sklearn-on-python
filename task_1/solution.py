import pandas as pd 

data = pd.read_csv('train.csv')
    
pclass_1 = data[data.Pclass == 1][['Survived', 'Sex']]
pclass_2 = data[data.Pclass == 2][['Survived', 'Sex']]
pclass_3 = data[data.Pclass == 3][['Survived', 'Sex']]  

pclass_1_male = pclass_1[pclass_1.Sex == "male"][['Survived']]
pclass_1_male = pclass_1_male.groupby(['Survived'])['Survived'].count()
pclass_1_male.name = "Survived MALE for Pclass == 1"
print(pclass_1_male, "\n")

pclass_1_female = pclass_1[pclass_1.Sex == "female"][['Survived']]
pclass_1_female = pclass_1_female.groupby(['Survived'])['Survived'].count()
pclass_1_female.name = "Survived FEMALE for Pclass == 1"
print(pclass_1_female, "\n")

pclass_2_male = pclass_2[pclass_2.Sex == "male"][['Survived']]
pclass_2_male = pclass_2_male.groupby(['Survived'])['Survived'].count()
pclass_2_male.name = "Survived MALE for Pclass == 2"
print(pclass_2_male, "\n")

pclass_2_female = pclass_2[pclass_2.Sex == "female"][['Survived']]
pclass_2_female = pclass_2_female.groupby(['Survived'])['Survived'].count()
pclass_2_female.name = "Survived FEMALE for Pclass == 2"
print(pclass_2_female, "\n")

pclass_3_male = pclass_3[pclass_3.Sex == "male"][['Survived']]
pclass_3_male = pclass_3_male.groupby(['Survived'])['Survived'].count()
pclass_3_male.name = "Survived MALE for Pclass == 3"
print(pclass_3_male, "\n")

pclass_3_female = pclass_3[pclass_3.Sex == "female"][['Survived']]
pclass_3_female = pclass_3_female.groupby(['Survived'])['Survived'].count()
pclass_3_female.name = "Survived FEMALE for Pclass == 3"
print(pclass_3_female)

