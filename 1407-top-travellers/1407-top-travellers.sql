/* Write your PL/SQL query statement below */
SELECT u.name, NVL(SUM(r.distance),0) as travelled_distance
FROM Users u LEFT JOIN Rides r 
ON u.id = r.user_id
GROUP BY u.name, u.id
ORDER BY 2 DESC, u.name
