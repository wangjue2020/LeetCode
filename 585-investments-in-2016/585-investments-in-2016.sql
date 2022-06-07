# Write your MySQL query statement below

select round(sum(tiv_2016),2) as tiv_2016
from
(select pid, concat(lat, lon) as address from insurance group by address having count(address) <=1) as a join
(select distinct i1.pid, i1.tiv_2016
from insurance i1, insurance i2 
where i1.pid != i2.pid and i1.tiv_2015 = i2.tiv_2015) as b on a.pid = b.pid; 