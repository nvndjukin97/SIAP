import pandas as pd

dt = pd.read_csv("../data/Heart_disease_cleveland_new.csv")
dt.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

dt['cp'] = dt['cp'].astype('object')
dt['restecg'] = dt['restecg'].astype('object')
dt['slope'] = dt['slope'].astype('object')
dt['thal'] = dt['thal'].astype('object')

# Type of chest pain experienced by patient. This term categorized into 4 category.
# 0 typical angina, 1 atypical angina, 2 non- anginal pain, 3 asymptomatic (Nominal)
dt.loc[dt['cp'] == 0, 'cp'] = 'typical angina'
dt.loc[dt['cp'] == 1, 'cp'] = 'atypical angina'
dt.loc[dt['cp'] == 2, 'cp'] = 'non-anginal pain'
dt.loc[dt['cp'] == 3, 'cp'] = 'asymptomatic'

# Result of electrocardiogram while at rest are represented in 3 distinct values
# 0 : Normal 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of >
# 0.05 mV) 2: showing probable or definite left ventricular hypertrophyby Estes' criteria (Nominal)
dt.loc[dt['restecg'] == 0, 'restecg'] = 'normal'
dt.loc[dt['restecg'] == 1, 'restecg'] = 'ST-T wave abnormality'
dt.loc[dt['restecg'] == 2, 'restecg'] = 'left ventricular hypertrophy'

# ST segment measured in terms of slope during peak exercise
# 0: up sloping; 1: flat; 2: down sloping(Nominal)
dt.loc[dt['slope'] == 0, 'slope'] = 'upsloping'
dt.loc[dt['slope'] == 1, 'slope'] = 'flat'
dt.loc[dt['slope'] == 2, 'slope'] = 'downsloping'

# 1: normal blood flow 2: fixed defect (no blood flow in some part of the heart)
# 3: reversible defect (a blood flow is observed but it is not normal(nominal)
dt.loc[dt['thal'] == 1, 'thal'] = 'normal blood flow'
dt.loc[dt['thal'] == 2, 'thal'] = 'fixed defect'
dt.loc[dt['thal'] == 3, 'thal'] = 'reversible defect'


dt["sex"] = dt.sex.apply(lambda  x:'male' if x==1 else 'female')
dt['fbs'] = dt.fbs.apply(lambda  x: 'Yes' if x==1 else 'No')
dt['exang'] = dt.exang.apply(lambda  x: 'Yes' if x==1 else 'No')

dt.to_csv("../data/processed_cleveland.csv", index=False)