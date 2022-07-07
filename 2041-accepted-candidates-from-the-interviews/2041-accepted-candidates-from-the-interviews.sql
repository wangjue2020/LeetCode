# Write your MySQL query statement below
select candidate_id from candidates c left join rounds using(interview_id) where years_of_exp >= 2 group by candidate_id, interview_id having sum(score) > 15;