# Write your MySQL query statement below
select "failed" as period_state, min(fail_date) as start_date, max(fail_date) as end_date
from (select *, datediff(fail_date, date_add('2019-01-01', interval row_number()over(order by fail_date asc) day)) as period from failed where fail_date between date('2019-01-01') and date('2019-12-31')) P group by period 

union

select "succeeded" as period_state, min(success_date) as start_date, max(success_date) as end_date from (select *, datediff(success_date,date_add('2019-01-01', interval row_number()over(order by success_date asc) day)) as period from succeeded where success_date between date('2019-01-01') and date('2019-12-31')) s group by period

order by start_date;

# select *,row_number()over(order by fail_date asc), datediff(fail_date, (DATE_ADD(day, row_number()over(order by fail_date asc), '2019-01-01'))) as period from failed where fail_date between date('2019-01-01') and date('2019-12-31')
# select fail_date, datediff(fail_date, date_add('2019-01-01', interval row_number()over(order by fail_date asc) day))
# from failed where fail_date between date('2019-01-01') and date('2019-12-31')