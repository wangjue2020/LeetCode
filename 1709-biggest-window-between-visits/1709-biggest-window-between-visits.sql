# Write your MySQL query statement below
select today.user_id, 
(
    case when today.today_diff > ifnull(be.diff,0) then today.today_diff
    else ifnull(be.diff,0)
    end
) as biggest_window
from 

(select user_id, datediff(date('2021-01-01'), max(visit_date)) as today_diff
from uservisits
group by user_id) today 

left join 

(select user_id, max(diff) as diff from (select u1.user_id,  datediff(min(u2.visit_date),u1.visit_date) as diff
from UserVisits u1, UserVisits u2
where u1.user_id = u2.user_id and u1.visit_date < u2.visit_date
group by u1.user_id, u1.visit_date) t
group by user_id
)  be on today.user_id = be.user_id
# select user_id, max(diff) as diff from (select u1.user_id,  datediff(min(u2.visit_date),u1.visit_date) as diff
# from UserVisits u1, UserVisits u2
# where u1.user_id = u2.user_id and u1.visit_date < u2.visit_date
# group by u1.user_id, u1.visit_date) t
# group by user_id


# select u4.user_id, 
# (case when datediff(date('2021-01-01'), max(visit_date)) < u3.diff then u3.diff
# else datediff(date('2021-01-01'), max(visit_date))
# end) as biggest_window, u3.diff,  datediff(date('2021-01-01'), max(visit_date)) 
# from uservisits u4 left join (select u1.user_id,  datediff(min(u2.visit_date),u1.visit_date) as diff
# from UserVisits u1, UserVisits u2
# where u1.user_id = u2.user_id and u1.visit_date < u2.visit_date
# group by u1.user_id, u1.visit_date) u3 on u3.user_id = u4.user_id
# group by u3.user_id

