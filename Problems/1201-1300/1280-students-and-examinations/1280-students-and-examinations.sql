# # Write your MySQL query statement below
# select *
# from students st, subjects su left join examinations e 
# where st.student_id = e.student_id
# # group by st.student_id, st.student_name, subject_name
select t1.student_id, t1.student_name, t1.subject_name, count(e.student_id) as attended_exams
from (select * from students, subjects) t1 left join examinations e using(student_id, subject_name)
group by t1.student_id, t1.student_name, t1.subject_name
order by t1.student_id, t1.subject_name