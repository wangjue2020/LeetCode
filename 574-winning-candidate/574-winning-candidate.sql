# Write your MySQL query statement below
select  c.name from vote join Candidate c on vote.candidateId=c.id group by candidateId order by count(candidateId) desc limit 1