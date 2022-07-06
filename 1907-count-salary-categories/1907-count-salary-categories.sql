# Write your MySQL query statement below
with tmp as 
(select 1 as type, 'Low Salary' as category
union 
select 2 as type, 'Average Salary' as category
union
select 3 as type, 'High Salary' as category)

# select * from tmp;
select category, count(account_id) as accounts_count
from tmp left join (select *, case when income < 20000 then 'Low Salary' when income >= 20000 and income <= 50000 then 'Average Salary' else 'High Salary' end as category from accounts) t using(category)
group by category
