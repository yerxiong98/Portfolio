# Dealership Car Sales Project

#Tableau - https://public.tableau.com/app/profile/yer.xiong/viz/DealershipReport/Dashboard1?publish=yes

#TLDR - In my previous projects I didn't know what the purpose of using a cte was and how much more organized and easier it was than making multiple subqueries in the same select code. Just a 
#project with a lot more practice with cleaning data. There is still a lot more that I need to work on with cleaning data. My next project will probably be working with dirty data. A lot more 
#experience with using CTEs, CASE, subqueries. 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Simple cleanup on file car_sales_1.csv



import pandas as pd

#nans function to return any rows that had any null values in them so I could decide what I wanted to do to them
#I used this function on other python cleaning code except this one but I wanted to write this function here in case I needed it.
def nans(df): 
    return df[df.isnull().any(axis=1)]


cs = pd.read_csv('C:/Users/yerxiong98/Desktop/project/car/car_sales_1.csv')

#change format from dd/mm/yyyy to yyyy/mm/dd
cs['Date']=pd.to_datetime(cs['Date'],dayfirst=True)

#engine name had a different name for it so I replaced it with a simpler term
cs['Engine'] = cs['Engine'].str.replace('DoubleÂ','Dual')
cs.drop_duplicates(inplace=True)


cs['Customer Name'].fillna('Unknown',inplace=True)
cs['CouncilArea'].fillna('Unknown',inplace=True)

cs.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/car_sales_1.csv', index=False, sep=',')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

MYSQL 


create database cars;


use cars;


create table up_car_sales
(
date date,
customer_name varchar(100),
dealer_name varchar(100),
company varchar(100),
model varchar(100),
year Year,
body_style varchar(100),
engine varchar(100),
transmission varchar(100),
color varchar(100),
price_in_thousands int,
dealer_add varchar(100),
customer_address varchar(100),
council_area varchar(100),
phone varchar(8),
gender varchar(30),
annual_income INT,
dealer_location varchar(100),
dealer_no varchar(11),
dealer_region varchar(50)
)


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/car_sales_1.csv'
INTO TABLE up_car_sales
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(date, customer_name,dealer_name,company,model,year,body_style,engine,transmission,color,price_in_thousands,dealer_add,customer_address,council_area,phone,gender,annual_income,dealer_location,dealer_no,dealer_region)




--@block I wanted to make another column that was just a concatenate of company, model, year, and transmission
update up_car_sales
set make_model_year_trans = concat(company,' ',model,' ',year,' ',transmission);
 
--@block
update car_models
set make_model_year_trans = concat(make,' ',model,' ',year,' ',transmission_type)







--@block Same as before, I wanted to have a unique identifier for each customer since this dataset did not have unique names
alter table up_car_sales
add cust_id varchar(100)

--@block
update up_car_sales
set cust_id = concat(customer_name,'-',phone)

-------------------------------------------------------------------------------------------------------------------------------------------------------
A couple queries that I decided not to use in my dashboard but may end up adding them, unsure

--@block which 10 make/model/year/trans made the most money in the last 12 months recorded?
select make_model_year_trans, sum(price_in_thousands) as total_made from up_car_sales
where date between '2017-3-17' and '2018-3-18'
group by make_model_year_trans
order by total_made desc
limit 10

--@block what year of cars not made in 2017 are still sold in 2017?
select distinct make_model_year_trans from up_car_sales
where year(date) = '2017'
and year <> '2017'


--@block list of customers who have not purchased the last year
select cust_id from up_car_sales
where date not between '2017-03-17' and '2018-03-18';




-------------------------------------------------------------------------------------------------------------------------------------------------------
Main queries that I used for the visualization

--@block what type of bodystyle/transmission/color do male/female prefer
select gender, body_style, transmission, color, count(body_style) as total_sold from up_car_sales
group by gender, body_style, transmission, color
order by gender desc, body_style asc, transmission asc;


--@block best selling company, model, year for each dealership
with cte as
(
select dealer_name, make_model_year_trans, count(make_model_year_trans) as amount from up_car_sales
group by make_model_year_trans, dealer_name
)

------------------------------------------
--@block Just to double check if my query was actually getting the data that I wanted
select dealer_name, make_model_year_trans from up_car_sales
where dealer_name like 'Buddy%'
and make_model_year_trans = 'Ford Expedition 2015 Auto'

--@block Just to double check if my query was actually getting the data that I wanted
select company, model, year, sum(price_in_thousands) from up_car_sales
where company = 'Audi'
and model = 'A6'
and year = 2016;
------------------------------------------



--@block most total made from cars for each company
with cte as 
(
    select company, model, sum(price_in_thousands) as total_made from up_car_sales
    group by company, model
    order by company asc, total_made desc
)

select company, model, max(total_made) as total_made_thousands from cte
group by company
order by company asc;


--@block
select sum(price_in_thousands) from up_car_sales
where company = 'Nissan'
and model = 'Pathfinder'

--@block best selling cars for each dealership
with cte as(
    select dealer_name, make_model_year_trans, company, count(make_model_year_trans) as total_sold from up_car_sales
    group by dealer_name, make_model_year_trans
    order by total_sold desc
)

select dealer_name, company, make_model_year_trans, max(total_sold) as amount_sold from cte
group by dealer_name
order by dealer_name asc;





--@block Just to double check if my query was actually getting the data that I wanted
select dealer_name, make_model_year_trans, count(make_model_year_trans) as total from up_car_sales
where dealer_name like 'Star%'
group by make_model_year_trans
order by total desc;


--@block total made for each year
select year(date), dealer_name, sum(price_in_thousands) from up_car_sales
group by year(date), dealer_name
order by dealer_name asc, year asc;

--@block quarterly sales each dealer
select dealer_name, sum(price_in_thousands), year(date),
case 
    when month(date) between 1 and 3 then 'Q1'
    when month(date) between 4 and 6 then 'Q2'
    when month(date) between 7 and 9 then 'Q3'
    else 'Q4'
    end as quarter
from up_car_sales
group by dealer_name, year(date), quarter
order by dealer_name asc, year(date) asc, quarter asc;

--@block
select dealer_name, sum(price_in_thousands) from up_car_sales
where dealer_name like 'Capitol%' 
and (month(date) = 1 or month(date) = 2 or month(date) = 3)
and year(date) = 2016

--@block
select dealer_name, sum(price_in_thousands) from up_car_sales
group by dealer_name

--@block quarterly sales for each company
select company, sum(price_in_thousands), year(date),
case 
    when month(date) between 1 and 3 then 'Q1'
    when month(date) between 4 and 6 then 'Q2'
    when month(date) between 7 and 9 then 'Q3'
    else 'Q4'
    end as quarter
from up_car_sales
group by company, year(date), quarter
order by company asc, year(date) asc, quarter asc;

--@block
select * from up_car_sales

--@block percentage of each car sold for pie?
with cte as (
select count(company) as total from up_car_sales
)

select company, count(company)/total as percent from up_car_sales, cte
group by company
order by percent desc;

--@block sales over time
select * from up_car_sales;








