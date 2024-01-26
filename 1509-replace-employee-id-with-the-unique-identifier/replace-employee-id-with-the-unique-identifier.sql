# Write your MySQL query statement below
select uni.unique_id, emp.name
from EmployeeUNI uni
right join Employees emp
ON uni.id = emp.id