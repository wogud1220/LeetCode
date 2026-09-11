/* Write your PL/SQL query statement below */
SELECT user_id as user_id, COUNT(*) as followers_count
FROM Followers
GROUP BY User_id
ORDER BY user_id