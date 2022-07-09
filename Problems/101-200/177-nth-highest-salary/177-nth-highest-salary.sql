CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
 declare M INT default N-1;
  RETURN (
      # Write your MySQL query statement below.
      select(
        select distinct salary from Employee order by salary desc limit 1 offset M
      )
  );
END