# Write your MySQL query statement below
select stock_name, sum(price) as capital_gain_loss
from (select stock_name, (
    case operation 
    when "Buy" then -1*price
    else
        price
    end
) as price
from Stocks ) as s
group by stock_name;