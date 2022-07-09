# Write your MySQL query statement below
select q.id, q.year, ifnull(npv,0) as npv from queries q left join npv using(id, year)