# Write your MySQL query statement below
with sub as (SELECT distinct l1.user_id as user1_id, l2.user_id as user2_id
FROM Listens l1
JOIN Listens l2
ON l1.song_id = l2.song_id AND l1.day = l2.day AND l1.user_id != l2.user_id
GROUP BY l1.user_id, l2.user_id, l1.day
HAVING count(distinct l1.song_id) >= 3
)
SELECT s.user1_id as user_id ,s.user2_id as recommended_id
FROM sub s
LEFT JOIN Friendship f1
ON s.user1_id = f1.user1_id and s.user2_id = f1.user2_id
LEFT JOIN Friendship f2
ON s.user1_id = f2.user2_id AND s.user2_id = f2.user1_id
WHERE f1.user2_id IS NULL and f2.user1_id IS NULL
