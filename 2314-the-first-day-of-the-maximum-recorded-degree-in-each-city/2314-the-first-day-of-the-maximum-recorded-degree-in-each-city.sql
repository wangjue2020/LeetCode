# Write your MySQL query statement below
select city_id, day, degree from
(select city_id, day, degree, row_number()over(partition by city_id order by degree desc, day asc) as ro from weather ) tmp where ro=1 order by city_id asc;