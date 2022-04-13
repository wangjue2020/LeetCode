# Write your MySQL query statement below
(select id, 'Root' as type from Tree where p_id is null)
union
(select distinct t1.id as id, 'Inner' as type from Tree t1 join Tree t2 where t1.p_id is not null and t1.id = t2.p_id)
union 
(select t1.id,
 (case  
    when p_id is null then 'Root' 
    else 'Leaf'
  end)as type 
 from Tree t1 where t1.id not in (select distinct p_id as id from Tree where p_id is not null))
