# Write your MySQL query statement below
select distinct p1.user_id
from purchases p1 join purchases p2 using(user_id)
where datediff(p2.purchase_date, p1.purchase_date) <= 7 and p2.purchase_id <> p1.purchase_id and p2.purchase_date >= p1.purchase_date
order by p1.user_id