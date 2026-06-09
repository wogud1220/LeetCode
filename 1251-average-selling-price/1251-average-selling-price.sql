/* Write your PL/SQL query statement below */
SELECT p.product_id, NVL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2),0) as average_price
FROM Prices p LEFT JOIN UnitsSold u ON u.purchase_date <= p.end_date and u.purchase_date >= p.start_date and p.product_id = u.product_id
GROUP BY p.product_id
