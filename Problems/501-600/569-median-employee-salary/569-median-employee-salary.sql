# Write your MySQL query statement below
with t as (select *, row_number()over(partition by company order by salary) as ra from employee),
median as (select company, round(count(id)/2) as fi, round((count(id)+1)/2) as se from t group by company 
)
select id, company, salary from t left join median m using(company) where ra between fi and se;