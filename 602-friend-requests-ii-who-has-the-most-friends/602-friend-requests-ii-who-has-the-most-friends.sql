# Write your MySQL query statement below
select requester_id as id, count(*) as num from (select accepter_id as requester_id, requester_id as accepter_id from requestaccepted
union 
select requester_id, accepter_id from requestaccepted) a
group by a.requester_id
order by num desc limit 1;