# Write your MySQL query statement below
select distinct t.id,
    (case
    when t.p_id is null then "Root"
    when t1.p_id is not null then "Inner"
     else "Leaf"
    end) as type
from Tree t left join Tree t1 on t.id=t1.p_id;
