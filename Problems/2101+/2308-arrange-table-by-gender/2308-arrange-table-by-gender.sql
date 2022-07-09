# Write your MySQL query statement below
select * from Genders order by row_number() over (partition by gender order by user_id asc)  asc, gender asc