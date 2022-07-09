# Write your MySQL query statement below
select ad_id, 
case 
    when 
        sum(case when action='Clicked' or action='Viewed' then 1 else 0 end) = 0 then 0 
    else 
        round(100*sum(case when action='Clicked' then 1 else 0 end) / sum(case when action='Clicked' or action='Viewed' then 1 else 0 end),2 )
end
as ctr
from ads
group by ad_id
order by ctr desc, ad_id asc;