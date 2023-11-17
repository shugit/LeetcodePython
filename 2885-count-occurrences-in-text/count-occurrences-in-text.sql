# Write your MySQL query statement below
with sub as (SELECT file_name, 
CASE WHEN content LIKE '% bull %' THEN 1 ELSE 0 END as bullc, 
CASE WHEN content LIKE '% bear %' THEN 1 ELSE 0 END as bearc
FROM Files)
SELECT 'bull' as word, (SELECT sum(bullc) from sub) as count
union all
SELECT 'bear' as word, (SELECT sum(bearc) from sub) as count