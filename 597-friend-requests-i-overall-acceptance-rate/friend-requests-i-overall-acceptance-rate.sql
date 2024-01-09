SELECT COALESCE(round(a.total/b.total,2),0) as accept_rate
FROM (
    SELECT COALESCE(count(*),0) as total
    FROM (SELECT * FROM RequestAccepted
    GROUP BY requester_id, accepter_id) m
) a
JOIN (
    SELECT COALESCE(count(*),0) as total
    FROM ( SELECT *
    FROM FriendRequest
    GROUP BY sender_id, send_to_id) k
) b