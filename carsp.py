import pandas as pd

def nans(df): 
    return df[df.isnull().any(axis=1)]


cs = pd.read_csv('C:/Users/yerxiong98/Desktop/project/car/car_sales_1.csv')
cs['Date']=pd.to_datetime(cs['Date'],dayfirst=True)
cs['Engine'] = cs['Engine'].str.replace('DoubleÂ','Dual')
cs.drop_duplicates(inplace=True)
cs['Customer Name'].fillna('Unknown',inplace=True)
cs['CouncilArea'].fillna('Unknown',inplace=True)

cs.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/car_sales_1.csv', index=False, sep=',')
