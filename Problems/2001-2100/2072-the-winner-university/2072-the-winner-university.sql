# Write your MySQL query statement below
with a as 
(select count(student_id) as n from NewYork where score >= 90), 
b as (select count(student_id) as c from California where score >= 90)

select case when n > c then 'New York University' when n=c then 'No Winner' else 'California University' end as winner from a,b