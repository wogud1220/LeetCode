/* Write your PL/SQL query statement below */
SELECT p.product_name, Sum(o.unit) as unit
FROM Products p, Orders o
WHERE p.product_id = o.product_id and o.order_date <='2020-02-29' and o.order_date >= '2020-02-01' 
GROUP BY p.product_name
Having Sum(o.unit) >= 100;