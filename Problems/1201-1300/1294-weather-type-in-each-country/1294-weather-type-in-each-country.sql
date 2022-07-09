# Write your MySQL query statement below
select country_name, case when avg(weather_state) <=15 then 'Cold' when avg(weather_state) >= 25 then 'Hot' else 'Warm' end as weather_type
from weather join Countries using(country_id)
where substring(day, 1,7) = '2019-11'
group by weather.country_id