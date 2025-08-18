import pandas as pd

dt = pd.read_csv("../data/framingham.csv")
dt.columns = ['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp',
       'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose', 'TenYearCHD']

dt['cigsPerDay'] = dt['cigsPerDay'].fillna(0)
dt['totChol'] = dt['totChol'].fillna(0)
dt['BMI'] = dt['BMI'].fillna(0)
dt['heartRate'] = dt['heartRate'].fillna(0)
dt['glucose'] = dt['glucose'].fillna(0)

dt['male'] = dt.male.apply(lambda  x: 'Female' if x==1 else 'Male')
dt['currentSmoker'] = dt.currentSmoker.apply(lambda  x: 'Yes' if x==1 else 'No')
dt['BPMeds'] = dt.BPMeds.apply(lambda  x: 'Yes' if x==1 else 'No')
dt['prevalentStroke'] = dt.prevalentStroke.apply(lambda  x: 'Yes' if x==1 else 'No')
dt['prevalentHyp'] = dt.prevalentHyp.apply(lambda  x: 'Yes' if x==1 else 'No')
dt['diabetes'] = dt.diabetes.apply(lambda  x: 'Yes' if x==1 else 'No')
dt['TenYearCHD'] = dt.TenYearCHD.apply(lambda  x: 'Yes' if x==1 else 'No')

# Replaces NaN values with the most frequent value
# dt['education'] = dt['education'].fillna(dt['education'].mode()[0])
dt['education'] = dt['education'].fillna(0)
dt['education'] = dt['education'].astype('object')
dt.loc[dt['education'] == 0, 'education'] = 'Unknown'
dt.loc[dt['education'] == 1, 'education'] = 'Elementary school'
dt.loc[dt['education'] == 2, 'education'] = 'Some high school (up to 12th grade, no diploma)'
dt.loc[dt['education'] == 3, 'education'] = 'High school graduate'
dt.loc[dt['education'] == 4, 'education'] = 'College or higher education'

dt.to_csv("../data/processed_framingham.csv", index=False)