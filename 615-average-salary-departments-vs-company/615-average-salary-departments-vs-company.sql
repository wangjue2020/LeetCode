# Write your MySQL query statement below
with company_avg as (select date_format(pay_date, '%Y-%m') as pay_month, avg(amount) as company_mean from salary group by pay_month)

select pay_month, department_id, case when department_avg >company_mean then 'higher' when department_avg = company_mean then 'same' else 'lower' end as comparison
from (select date_format(pay_date, '%Y-%m') as pay_month, department_id, avg(amount) as department_avg from employee e left join salary s using(employee_id) group by department_id, pay_month) t left join company_avg using(pay_month)