# Write your MySQL query statement below
# select case when duration < 300 then '[0-5>' when duration <600 then '[5-10>' when duration <900 then '[10-15>' else '15 or more' end as bin, session_id from sessions 

with bintable as 
(
select '[0-5>' as bin 
union 
select '[5-10>' as bin 
union 
select '[10-15>' as bin 
union 
select '15 or more' as bin ),
tmp as ( select case when duration < 300 then '[0-5>' when duration <600 then '[5-10>' when duration <900 then '[10-15>' else '15 or more' end as bin, session_id from sessions 
)
select bin, count(session_id) as total from bintable left join tmp using(bin) group by bin