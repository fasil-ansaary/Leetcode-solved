# Write your MySQL query statement below
select a.name, b.bonus as bonus from Employee a
left join Bonus b on a.empId = b.empId
where bonus < 1000 or bonus is null
