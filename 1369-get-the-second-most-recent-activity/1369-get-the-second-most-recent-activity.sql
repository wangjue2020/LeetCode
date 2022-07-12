# Write your MySQL query statement below
with a as 
(select *
from (select *, row_number()over(partition by username order by endDate desc) as rn from userActivity) tmp
where rn <= 2)

select a.username, a.activity, a.startDate, a.endDate from a join (select username, max(rn) as rn from a group by username) a_max on a.rn=a_max.rn and a.username=a_max.username