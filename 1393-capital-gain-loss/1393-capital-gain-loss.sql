# Write your MySQL query statement below
select stock_name, sum(updated_price) as capital_gain_loss
from 
(select stock_name, 
    (case operation 
     when "Buy" then -1*price
     when "Sell" then price
     end
    ) as updated_price
from Stocks) as updated
group by stock_name