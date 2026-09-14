/* Write your PL/SQL query statement below */
SELECT employee_id
FROM Employees
WHERE salary < 30000 and
manager_id NOT IN 
(
SELECT employee_id
FROM Employees
)
and manager_id is NOT NULL
ORDER BY 1
