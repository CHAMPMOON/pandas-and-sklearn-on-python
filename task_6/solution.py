import pandas as pd  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression


data = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#   Заменяю на int чтобы работать с ними:
# Embarked: S == 1, C == 2, Q == 3
# Sex: male == 1, female == 2
data['Embarked'] = data.Embarked.apply(lambda x: 1 if x == "S" else 2 if x == "C" else 3)
data['Sex'] = data.Sex.apply(lambda x: 1 if x == "male" else 2)

test['Embarked'] = test.Embarked.apply(lambda x: 1 if x == "S" else 2 if x == "C" else 3)
test['Sex'] = test.Sex.apply(lambda x: 1 if x == "male" else 2)

# Удалить все значения NaN:
data = data.fillna(method='ffill')
test = test.fillna(method='ffill')

# Переменная X содержит все атрибуты / функции, а переменная y содержит метки.
X_train = data[['Pclass', 'Sex', 'Age', 'Embarked']].values
y = data['Survived'].values

# Затем мы разделяем данные на обучающий набор, и на набор тестов:
X_train, X_train_test, y_train, y_train_test = train_test_split(X_train, y, test_size = 0.33, random_state=0)

# Набор aтрибутов test.cvs:
X_test_test = test[['Pclass', 'Sex', 'Age',  'Embarked']].values

# Создадим и обучим нашу модель:
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

coeff_df = pd.DataFrame(regressor.coef_, [['Pclass', 'Sex', 'Age', 'Embarked']], columns=['Survived'])  

# Коэффициенты нашей регрессионной модели(как разные столбцы влияют на Survived)
print("Regression model coefficients:\n", coeff_df, "\n")

# Сделаем прогноз на тестовых данных train.cvs:
y_pred = regressor.predict(X_train_test)

# Округлим наши прогнозируемые значения для сравнения с фактическими(не пользовался round):
for i in range(len(y_pred)): 
    if y_pred[i] >= 0.45: y_pred[i] = 1
    else: y_pred[i] = 0

df = pd.DataFrame({'Actual': y_train_test, 'Predicted': y_pred})
df1 = df.head(30)

#  Разница фактическим значением и прогнозируемым значением:
print("Difference between actual and predicted:\n", df1, "\n")

# Вычислим какой процент успешного прогнозирования:
size = len(y_pred)
count = 0
for i in range(len(y_pred)):
    if y_pred[i] == y_train_test[i]:
        count += 1

# Процент успешного прогнозирования( получилось 77.6% ):
print('Percentage of fidelity - ', count/size * 100, '%\n')

# Попытаемся предсказать выживаемость для пассажиров test.csv:
surv_pred = regressor.predict(X_test_test)
for i in range(len(surv_pred)): 
    if surv_pred[i] >= 0.45: surv_pred[i] = 1
    else: surv_pred[i] = 0

# Тесты для test.csv X_test_test идут по порядку, поэтому можно спокойно добавить столбец, не опасаюсь несостыковки:
test['Survived'] = surv_pred
print("Final table test with new column Survived:\n", test)
# В итоге я предсказал выживаемость каждого пассажира с точностью в 77.6%
