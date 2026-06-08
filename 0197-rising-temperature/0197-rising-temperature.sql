/* Write your PL/SQL query statement below */
SELECT w1.id
FROM Weather w1 JOIN Weather w2 ON w1.recordDate = w2.recordDate + 1 
--                                              오늘 어제
Where w1.temperature > w2.temperature