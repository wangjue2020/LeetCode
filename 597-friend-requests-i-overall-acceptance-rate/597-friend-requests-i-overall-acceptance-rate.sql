# Write your MySQL query statement below
# select ifnull(round(count( r.accepter_id)/count(*),2),0.00) as accept_rate
 select 
 ifnull(
     round(
         (select count(*) from (select distinct requester_id, accepter_id from requestAccepted) r)
         /
(select count(*) from (select distinct sender_id, send_to_id from friendrequest) f), 2), 0.00) as accept_rate




