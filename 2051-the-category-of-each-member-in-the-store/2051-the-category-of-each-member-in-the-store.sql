# Write your MySQL query statement below
select member_id, name,  
case 
when  100*count(p.visit_id)/count(v.visit_id) is null then 'Bronze'
when 100*count(p.visit_id)/count(v.visit_id) >= 80 then 'Diamond' 
when 100*count(p.visit_id)/count(v.visit_id) >= 50 then 'Gold' 
# when ifnull(100*count(p.visit_id)/count(v.visit_id),0) < 50 then 'Silver'
else 'Silver' 
end as category 
from Members left join visits v using(member_id) left join Purchases p using(visit_id) group by member_id order by member_id;