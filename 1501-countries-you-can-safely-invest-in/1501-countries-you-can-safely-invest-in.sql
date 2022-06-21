# Write your MySQL query statement below

# select avg(duration) as global_avg from calls;

# select substring(phone_number, 1,3) as country_code from person;

select  country.name as country
from 
(select caller_id as id, duration from calls 
union 
select callee_id as id, duration from calls) new_calls left join 
(select id, substring(phone_number, 1,3) as country_code from person) new_person on new_calls.id = new_person.id left join Country on new_person.country_code=country.country_code
group by new_person.country_code
having avg(new_calls.duration) > (select avg(duration) as global_avg from calls)