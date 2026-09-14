/* Write your PL/SQL query statement below */


SELECT u.name, t.balance
FROM (
SELECT account, SUM(amount) as balance
FROM Transactions
GROUP BY account
HAVING SUM(amount) > 10000
) t JOIN Users u ON t.account = u.account

