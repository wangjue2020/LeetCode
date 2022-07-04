# Write your MySQL query statement below
# select user_id, user_name, credit - ifnull(sum(t1.amount),0 )+ ifnull(sum(t2.amount),0) as credit, case when credit - ifnull(sum(t1.amount),0 )+ ifnull(sum(t2.amount),0) < 0 then 'Yes' else 'No' end as credit_limit_breached
# from users u left join transactions t1 on u.user_id = t1.paid_by left join transactions t2 on u.user_id = t2.paid_to
# group by user_id


select user_id, user_name, credit - ifnull(out_amount,0) + ifnull(in_amount,0) as credit, case when credit - ifnull(out_amount,0) + ifnull(in_amount,0) >= 0 then 'No' else 'Yes' end as credit_limit_breached from users u left join 
(select paid_by as user_id, sum(amount) as out_amount from transactions group by paid_by) pb using (user_id) left join
(select paid_to as user_id, sum(amount) as in_amount from transactions group by paid_to
) pt using(user_id)
