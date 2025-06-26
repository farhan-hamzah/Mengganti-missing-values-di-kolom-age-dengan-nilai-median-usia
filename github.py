import pandas as pd
data = pd.read_csv('kapal_titanic.csv')
isna = data[data['age'].isnull()]
med = data['age'].median()
isna['age'].fillna(med, inplace=True)
print(isna['age'])