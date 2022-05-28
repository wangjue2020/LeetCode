# Write your MySQL query statement below
# select score, id, rank() over(order by score) rank from Scores 

select score, rk as "rank"
from (SELECT score, DENSE_RANK() OVER(order by score desc) rk  FROM scores) as s;