# Write your MySQL query statement below
with low_high_exam as 
(select exam_id, min(score) as low, max(score) as high from exam group by exam_id)

select distinct student_id, student_name from exam e join student using(student_id) where e.student_id not in (select distinct student_id from exam left join low_high_exam using(exam_id)
where score = low or score = high)
order by student_id