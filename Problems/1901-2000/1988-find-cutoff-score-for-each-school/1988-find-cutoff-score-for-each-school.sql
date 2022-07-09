# Write your MySQL query statement below
select school_id, ifnull(score,-1) as score
from (select schools.*, exam.*, row_number() over (partition by school_id order by student_count desc, score asc) as ra from schools left join exam on student_count <= capacity) t
where ra = 1 or ra is null

