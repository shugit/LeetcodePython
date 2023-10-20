# Write your MySQL query statement below
 with salary as (
    SELECT employee_id, experience, sum(salary) over (partition by experience order by salary, employee_id) as acc
    FROM Candidates
    order by experience, acc
)
, rest as (
   SELECT COALESCE(
       (select 70000 - acc
    from salary
    where acc <= 70000 and experience = 'Senior'
    order by acc desc limit 1)
    , 70000) as rest
)
, cate as 
(SELECT 'Senior' as experience
UNION ALL
SELECT 'Junior' as experience
), s as (SELECT experience, count(*) as count
FROM salary 
WHERE 
CASE WHEN experience ='Senior' 
THEN acc <= 70000 ELSE acc <= (select rest from rest) END
GROUP BY experience
)
select c.experience, COALESCE(s.count, 0) as accepted_candidates 
FROM cate c
LEFT JOIN s
ON c.experience = s.experience