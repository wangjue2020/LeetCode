# Write your MySQL query statement below
select s1.id, (
    case 
    when s1.id%2=1 and s2.student is not NULL then s2.student
    when s1.id%2=1 and s2.student is NULL then s1.student
    else s3.student
    end
) as student
from Seat s1 left join Seat s2 on s1.id+1 = s2.id
    left join Seat s3 on s3.id+1 = s1.id
