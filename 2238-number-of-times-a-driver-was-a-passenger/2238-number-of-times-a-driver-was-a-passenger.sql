# Write your MySQL query statement below
select r1.driver_id, count(r2.ride_id) as cnt from (select distinct driver_id from rides) r1 left join rides r2 on r1.driver_id = r2.passenger_id group by r1.driver_id;

