# Write your MySQL query statement below
# report the names of all the salespersons who did not have any orders related to the company with the name "RED".
select name
from SalesPerson sp
where sp.sales_id not in 
(select distinct s.sales_id
from SalesPerson s join Orders o on s.sales_id=o.sales_id
    join Company c on o.com_id=c.com_id
where c.name="RED")