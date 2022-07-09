# Write your MySQL query statement below
select  e1.student_id, min(e1.course_id) as course_id, e1.grade  from enrollments e1 join (select student_id, max(grade) as grade from enrollments group by student_id) e2 using(student_id)
where e1.grade = e2.grade
group by e1.student_id
order by e1.student_id