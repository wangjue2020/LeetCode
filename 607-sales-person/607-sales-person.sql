# Write your MySQL query statement below
# report the names of all the salespersons who did not have any orders related to the company with the name "RED".
select name from salesperson where name not in 
(select s.name from Orders o left join Company c on o.com_id = c.com_id
left join SalesPerson s on o.sales_id = s.sales_id where c.name='RED')