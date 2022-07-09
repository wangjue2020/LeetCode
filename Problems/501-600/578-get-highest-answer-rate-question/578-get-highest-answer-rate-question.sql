select a.question_id as survey_log from (select question_id, count(answer_id) as a from surveylog where action="answer" group by question_id) as A
right join 
(select question_id, count(question_id) as s from surveylog where action="show" group by question_id) as B on a.question_id=b.question_id
order by ifnull(a.a,0)/ b.s desc , a.question_id asc limit 1;