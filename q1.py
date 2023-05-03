import pandas as pd

abortionLegal = pd.read_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q1.csv', sep= ',')
abortionLegal['Year'] = abortionLegal['Year'].str[:4]
abortionLegal = abortionLegal.drop_duplicates()

#abortionLegal = abortionLegal.dropna() drop any rows with empty values
#abortionLegal.fillna(" ",inplace= True) fill rows with empty values with " "

print(abortionLegal)

abortionLegal.to_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q1.csv',sep= '\t', index= False)


