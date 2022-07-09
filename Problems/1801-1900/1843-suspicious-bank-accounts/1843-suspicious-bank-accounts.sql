# Write your MySQL query statement below
with tmp as 
(select account_id, sum(amount) as amount, extract(year from day) as year, extract(month from day) as month  from transactions where type="Creditor" group by account_id, year, month)

select distinct t1.account_id
from tmp t1, tmp t2, accounts a
where t1.account_id = t2.account_id and ((t1.year=t2.year and t1.month+1 = t2.month) or (t1.year+1 = t2.year and t1.month=12 and t2.month=1)) and a.account_id = t1.account_id and t1.amount >max_income and t2.amount>max_income order by t1.account_id asc;