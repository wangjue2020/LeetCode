# Write your MySQL query statement below
select round(min(distance),2) as shortest from (select p1.x, p1.y, sqrt(power(p2.x-p1.x,2) + power(p2.y-p1.y, 2)) as distance
from point2d p1, point2d p2
where p1.x != p2.x or p1.y != p2.y) distance

# select p1.x, p1.y,p2.x, p2.y, sqrt(power(p2.x-p1.x,2) + power(p2.y-p1.y, 2)) as distance
# from point2d p1, point2d p2
# where p1.x != p2.x or p1.y != p2.y