# Write your MySQL query statement below
with max_sa as (select company_id, max(salary) as salary_max from salaries group by company_id)

select salaries.company_id, employee_id, employee_name, round(case when salary_max<1000 then salary when salary_max <=10000 then salary*0.76 else salary*0.51 end) as salary from salaries left join max_sa using(company_id)