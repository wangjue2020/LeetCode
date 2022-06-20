# Write your MySQL query statement below
select count(distinct s.account_id) as accounts_count
# select s.account_id
from subscriptions s left join streams st on s.account_id = st.account_id
where extract(year from end_date) ="2021" and st.stream_date not between date("2021-01-01") and date("2021-12-31")