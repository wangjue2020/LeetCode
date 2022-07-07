# Write your MySQL query statement below
with f as (select first_col, row_number()over(order by first_col asc) as r from data),
s as (select second_col, row_number()over(order by second_col desc) as r from data)

select first_col, second_col from f join s using(r);
# select first_col, row_rank()over(order by first_col asc) as r from data