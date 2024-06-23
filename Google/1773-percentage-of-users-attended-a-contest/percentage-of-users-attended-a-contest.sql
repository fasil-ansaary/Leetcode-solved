# Write your MySQL query statement below
select b.contest_id, round(count(a.user_id)/(
    select count(*) from Users
)*100,2) as percentage
from Users a, Register b
where a.user_id = b.user_id
group by b.contest_id
order by percentage desc, b.contest_id 