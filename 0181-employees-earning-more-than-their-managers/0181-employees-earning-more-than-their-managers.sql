/* Write your PL/SQL query statement below */
SELECT E.name as Employee
FROM EMPLOYEE E, EMPLOYEE M
WHERE E.managerId = M.id and E.SALARY > M.SALARY;