-- Write your query below
SELECT seller_name
FROM seller
WHERE seller_id NOT IN (
    SELECT DISTINCT s.seller_id
    FROM orders AS o
    JOIN seller AS s ON o.seller_id = s.seller_id
    WHERE o.sale_date BETWEEN '2020-01-01' AND '2020-12-31'
)
ORDER BY seller_name;