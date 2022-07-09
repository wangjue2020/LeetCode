# Write your MySQL query statement below
(select name as results from movierating join users using(user_id) group by user_id order by count(movie_id) desc,results asc limit 1)
union
select results from
(select title as results, avg(rating) as ar from movierating join movies using(movie_id) where created_at between date('2020-02-01') and date('2020-02-28') group by movie_id order by ar desc, results asc limit 1) t;