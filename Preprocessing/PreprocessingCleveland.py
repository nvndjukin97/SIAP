import pandas as pd

# 1) Ucitavanje
dt = pd.read_csv("../data/Heart_disease_cleveland_new.csv")
# 2) Setovanje imena kolona
dt.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# 3) Kolone sa  "?" kao nedostajuca vrednost
dt = dt.replace("?", pd.NA)

print("=== Missing values BEFORE type fixes ===")
print(dt.isnull().sum())
print("Rows:", len(dt))

# 4) Ensure numeric columns are numeric (convert invalid -> NaN)
#    ca and thal are the usual offenders; we also force all numeric-looking cols.
numeric_cols = ['age', 'sex', 'trestbps', 'chol', 'fbs', 'thalach', 'exang', 'oldpeak', 'ca', 'thal', 'target']
for col in numeric_cols:
    dt[col] = pd.to_numeric(dt[col], errors='coerce')

print("\n=== Missing values AFTER numeric coercion ===")
print(dt.isnull().sum())
print("Rows:", len(dt))

# 5) Handle missing values
# Option A (recommended for Cleveland): drop rows with any missing values
dt_before = len(dt)
dt = dt.dropna()
dt_after = len(dt)

print(f"\nDropped rows due to missing values: {dt_before - dt_after}")
print("Rows after dropna:", len(dt))
print("=== Missing values FINAL ===")
print(dt.isnull().sum())


# 6) Konvertovanje kolona u kategoricke
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

print("Final shape:", dt.shape)
print("Target distribution:\n", dt["target"].value_counts(normalize=True))