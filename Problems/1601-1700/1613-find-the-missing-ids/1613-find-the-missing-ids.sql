# Write your MySQL query statement below
with recursive ids as (
select 1 as id 
union all
select id+1 as id from ids where id<(select max(customer_id) from customers))

select id as ids from ids
where id not in (select customer_id from customers)
order by ids asc