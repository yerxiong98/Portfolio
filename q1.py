#Abortion Data

#TLDR

#Summary



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#"Q1 Should Abortions Be Legal?"
#Make dataframe from a csv file, format date values to just the years instead of actual dates, drop duplicates, drop rows with null values

import pandas as pd

#read the csv Q1 with separators ',' into abortionLegal dataframe
abortionLegal = pd.read_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q1.csv', sep= ',')

#change the year column from a full date to just the years
abortionLegal['Year'] = abortionLegal['Year'].str[:4]

#drop duplicates in dataframe
abortionLegal = abortionLegal.drop_duplicates()

#abortionLegal = abortionLegal.dropna()  If I want to drop rows with null values, probably not the best idea for a small dataset like this and this dataset is based off years
#abortionLegal.fillna(" ",inplace= True) If I wanted to fill the null rows with a value " "
print(abortionLegal)

#save abortionLegal df as a csv with separator '\t' which is the default and index false to get rid of the first column
abortionLegal.to_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q1.csv',sep= '\t', index= False)

"""

MYSQL

--create database abortion to store all my tables
create database abortion;

--create table abortion_legal
create table abortion_legal
(
Year year,
legal_any int,
legal_certain int,
illegal_any	int,
no_opinion int
);

--LOAD DATA to abortion_legal table
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q1.csv'
INTO TABLE abortion_legal
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(year, legal_any, legal_certain, illegal_any, no_opinion);
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Q2 Prochoice, Prolife, Neither, Don't Know Meaning?
# This code is almost identical to Q1 except .copy(deep=True). 
import pandas as pd

pro_what = pd.read_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q2.csv')

#I wanted to try making a deep copy of the dataframe instead of new_pro_what = pro_what which wouldn't make a new copy but just reference pro_what
new_pro_what= pro_what.copy(deep=True)
new_pro_what['Year'] = new_pro_what['Year'].str[:4]

new_pro_what.drop_duplicates(inplace=True)
new_pro_what.dropna(inplace=True)

#Just to see what the table looks like before saving it to a csv
print(new_pro_what)

new_pro_what.to_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q2.csv', sep= '\t', index= False)

"""

MYSQL

--create table pro_what to store data from csv
create table pro_what
(
Year year,
pro_choice int,
pro_life int,
mixed_neither int,
dont_know_terms int,
no_opinion int
);

--load data infile Q2 to table pro_what
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q2.csv'
INTO TABLE pro_what
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(year, pro_choice, pro_life, mixed_neither, dont_know_terms, no_opinion);

--Just to see the table
select * from pro_what;
"""


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#While I just finished cleaning the first two tables, I thought what if I tried to merge the two tables into one dataframe. I'm unsure if I should do this because 
#the two tables have a different amount of years for each dataset. Q1 goes back to 1975 and Q2 to 1995 so would there be a lot of null values from 1975-1995?
#I might just do a JOIN in SQL once I have all the data cleaned.*** Something I should research more about later though. ***

#Q3

















