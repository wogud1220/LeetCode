/* Write your PL/SQL query statement below */
SELECT user_id, MAX(time_stamp) as last_stamp
FROM Logins
WHERE time_stamp <'2021-01-01' and time_stamp >= DATE '2020-01-01'
GROUP BY user_id