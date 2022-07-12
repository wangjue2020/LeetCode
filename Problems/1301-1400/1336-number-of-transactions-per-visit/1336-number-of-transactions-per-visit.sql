# Write your MySQL query statement below
with recursive b as (
    select 0 as transactions_count
    union all
    select transactions_count+1 from b where transactions_count < (select max(tran) from (select v.user_id, v.visit_date, count(t.user_id) as tran from visits v left join transactions t on v.user_id=t.user_id and v.visit_date=t.transaction_date
group by v.user_id, v.visit_date) t)
)

select transactions_count, count(tmp.user_id) as visits_count from b left join (select v.user_id, v.visit_date, count(t.user_id) as tran from visits v left join transactions t on v.user_id=t.user_id and v.visit_date=t.transaction_date
group by v.user_id, v.visit_date) tmp on b.transactions_count=tmp.tran 
group by transactions_count
# select * from b