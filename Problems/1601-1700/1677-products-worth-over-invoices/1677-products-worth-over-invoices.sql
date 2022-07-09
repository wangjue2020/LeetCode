# Write your MySQL query statement below

select p.name, sum(ifnull(rest, 0)) as rest, sum(ifnull(paid, 0)) as paid, sum(ifnull(canceled, 0)) as canceled, sum(ifnull(refunded,0)) as refunded from product p left join invoice i on p.product_id=i.product_id group by p.product_id order by name