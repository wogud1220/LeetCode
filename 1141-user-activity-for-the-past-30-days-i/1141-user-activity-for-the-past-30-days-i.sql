/* Write your PL/SQL query statement below */
SELECT TO_CHAR(activity_date, 'YYYY-MM-DD') AS day, COUNT(distinct user_id) as active_users
FROM Activity
WHERE activity_date >= '2019-06-28' and activity_date <= '2019-07-27'
GROUP BY activity_date