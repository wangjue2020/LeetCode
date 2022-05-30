# Write your MySQL query statement below
select name from SalesPerson where sales_id not in
(select s.sales_id
from SalesPerson s left join Orders o on s.sales_id=o.sales_id
left join company c on c.com_id=o.com_id
where c.name="RED")