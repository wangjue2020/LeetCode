# Write your MySQL query statement below
select item_category as Category, sum(case when date_format(order_date, "%W") ='Monday' then quantity else 0 end) as Monday, sum(case when date_format(order_date, "%W") ='Tuesday' then quantity else 0 end) as Tuesday,
 sum(case when date_format(order_date, "%W") ='Wednesday' then quantity else 0 end) as Wednesday, sum(case when date_format(order_date, "%W") ='Thursday' then quantity else 0 end) as Thursday, sum(case when date_format(order_date, "%W") ='Friday' then quantity else 0 end) as Friday, sum(case when date_format(order_date, "%W") ='Saturday' then quantity else 0 end) as Saturday, sum(case when date_format(order_date, "%W") ='Sunday' then quantity else 0 end) as Sunday

from orders o right join items i using(item_id)
group by item_category
order by category