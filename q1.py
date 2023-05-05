#Abortion Data

#TABLEAU data visualization in works

#TLDR - Not much base python coding, good for basic pandas read_csv,to_csv,drop_duplicates,dropna

#Summary-
#    This project is my first time using python and pandas. Theres still so much I need to learn about python. This project didn't really have base python only coding
#but mainly pandas. The main functions that were used were read_csv, drop_duplicates, dropna, sep=, index=, dataframes. It was a good experience nonetheless since it 
#was just doing the same lines of code over and over to basically just nail in what those functions do. In between cleaning the data for SQL, I thought to myself 
#if I could just make a script where I could have multiple input()s to basicically get all the information about the name of the csv, location, etc along with 
#defined functions that I could call through the code. I kind of had a plan for my code and how I wanted to make it. When I was trying to get inputs for the csv name and
#file location, I was trying to make the function combine the inputs into a string to put as the read_csv(csvLocation+csvName) but it didn't work. I'm still unsure
#about if this is something that could work or if it is even worth doing since theres a lot things that different tables have that others don't



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

import pandas as pd

q3=pd.read_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q3.csv')
newq3 = q3.copy(deep=True)

newq3 = newq3.drop_duplicates()
newq3.dropna()
newq3['year'] = newq3['year'].str[:4]

newq3.to_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q3.csv', index= False)

"""

MYSQL

create table roe_v_wade
(
    year year,
    yes_overturn int,
    no_overturn int,
    no_opinion int
);

--i didnt notice this table was formated differently from the first two with fields terminated by ',' instead of '\t'
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q3.csv'
INTO TABLE roe_v_wade
fields terminated by ','
lines terminated by '\n'
IGNORE 1 LINES
(year, yes_overturn, no_overturn, no_opinion);

select * from roe_v_wade;

"""


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Q4

import pandas as pd

#I came into an issue while doing this one. For this one specifically, I had the csv file named Q4 at first in my directory. After cleaning up the data
#I just rewrote the dataframe over the Q4 csv instead of making a new one. I had messed up on the formatting of the table since I forgot to include the year
#column at first so the years became part of the index. So what I did was to rename the first file. I decided to change how I did this with Q7.
q4 = pd.read_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q4b.csv')
q4 = q4.drop_duplicates()
q4 = q4.dropna()
q4['year']=q4['year'].str[:4]
print(q4)

q4.to_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q4.csv', index=False)

"""

MYSQL

create table when_legal_illegal
(
    year year,
    f_3_legal int,
    f_3_illega int,
    f_3_circumstantial int,
    f_3_no_opinion int,
    s_3_legal int,
    s_3_illegal int,
    s_3_circumstantial int,
    s_3_no_opinion int,
    l_3_legal int,
    l_3_illegal int,
    l_3_circumstantial int,
    l_3_no_opinion int
)


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q4.csv'
INTO TABLE when_legal_illegal
fields terminated by ','
lines terminated by '\n'
IGNORE 1 lines
(year,f_3_legal,f_3_illega,f_3_circumstantial,f_3_no_opinion,s_3_legal,s_3_illegal,s_3_circumstantial,
s_3_no_opinion,l_3_legal,l_3_illegal,l_3_circumstantial,l_3_no_opinion)


-- I didn't realize that the column was named incorrectly so I just renamed it with ALTER, RENAME 
alter table when_legal_illegal
rename column f_3_illega to f_3_illegal;
"""


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Q6

import pandas as pd

q6 = pd.read_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q6b.csv')
q6 = q6.drop_duplicates()
q6 = q6.dropna()
q6['year'] = q6['year'].str[:4]

print(q6)

q6.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q6.csv',index=False)


"""

MYSQL

create table abortion_morality
(
    year year,
    moral_acceptable int,
    moral_wrong int,
    moral_situation int,
    no_opinion_or_no_moral_issue int
)


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q6.csv'
INTO TABLE abortion_morality
fields terminated by ','
lines terminated by '\n'
IGNORE 1 LINES
(year,moral_acceptable,moral_wrong,moral_situation,no_opinion_or_no_moral_issue)


select * from abortion_morality

"""

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Q7


import pandas as pd

q7 = pd.read_csv('C:/Users/yerxiong98/Desktop/project/abortion minimum/Q7.csv')
q7 = q7.drop_duplicates()
q7 = q7.dropna()

q7.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q7.csv', index=False)

"""

MYSQL

--
create table policy_satisfaction
(
    year year,
    satisfied int, 
    somewhat_satisfied int, 
    somewhat_dissastified int, 
    very_dissastified int, 
    no_opinion int
)

--
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/abortion/Q7.csv'
INTO TABLE policy_satisfaction
fields terminated by ','
lines terminated by '\n'
IGNORE 1 LINES
(year,satisfied, somewhat_satisfied, somewhat_dissastified, very_dissastified, no_opinion)

--
select * from abortion_legal
left join pro_what using (year)
left join roe_v_wade using (year)
left join abortion_morality using (year)
left join policy_satisfaction using (year)
"""

















