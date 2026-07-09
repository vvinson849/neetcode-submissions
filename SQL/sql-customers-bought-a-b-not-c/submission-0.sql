-- Write your query below
SELECT DISTINCT c.customer_id, c.customer_name
FROM customers AS c, orders AS o
WHERE c.customer_id = o.customer_id
AND c.customer_id NOT IN (SELECT customer_id FROM orders WHERE product_name LIKE 'C')
AND c.customer_id IN (SELECT a.customer_id 
                        FROM orders AS a, orders AS b 
                        WHERE a.customer_id = b.customer_id 
                        AND a.product_name LIKE 'A' 
                        AND b.product_name LIKE 'B')
ORDER BY c.customer_name;