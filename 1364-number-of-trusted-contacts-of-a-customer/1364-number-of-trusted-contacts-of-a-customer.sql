# Write your MySQL query statement below
select i.invoice_id, customer_name, price, contacts_cnt, trusted_contacts_cnt
from invoices i left join 
(select cu.customer_id, cu.customer_name, count(co.user_id) as contacts_cnt, sum(case when co.contact_email in (select email from customers) then 1 else 0 end) as trusted_contacts_cnt
from customers cu left join contacts co on cu.customer_id = co.user_id
group by cu.customer_id
) tmp on i.user_id= tmp.customer_id
order by invoice_id

# select cu.customer_id, cu.customer_name, count(co.user_id) as contacts_cnt, sum(case when co.contact_email in (select email from customers) then 1 else 0 end) as trusted_contacts_cnt
# from customers cu left join contacts co on cu.customer_id = co.user_id
# group by cu.customer_id