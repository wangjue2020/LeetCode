# Write your MySQL query statement below
with 
a as
(select substring(trans_date,1,7) as month, country, count(id) as approved_count, sum(amount) as approved_amount
from transactions 
where state='approved'
group by substring(trans_date,1,7), country
),
 b as
(select substring(c.trans_date,1,7) as month, country, count(trans_id) as chargeback_count, sum(amount) as chargeback_amount
from chargebacks c left join transactions on trans_id=id
group by substring(c.trans_date,1,7), country)

select a.month, a.country, approved_count, approved_amount, ifnull(chargeback_count,0) as chargeback_count,ifnull( chargeback_amount,0) as chargeback_amount from a left join b using(month, country)

union

select b.month, b.country, ifnull(approved_count,0) as approved_count, ifnull(approved_amount,0) as amount,chargeback_count, chargeback_amount from a right join b using(month, country)