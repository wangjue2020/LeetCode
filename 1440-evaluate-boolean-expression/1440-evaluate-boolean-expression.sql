# Write your MySQL query statement below
select e.left_operand, e.operator, e.right_operand, 
(case 
    when e.operator = '>' and v1.value>v2.value then 'true'
    when e.operator = '<' and v1.value <v2.value then 'true'
    when e.operator = '=' and v1.value = v2.value then 'true'
    else
        'false'
    end
) as value
from expressions e left join variables v1 on name = left_operand left join variables v2 on e.right_operand = v2.name