-- Write your query below
SELECT e.left_operand, e.operator, e.right_operand,
    CASE
        WHEN e.operator LIKE '<' THEN vl.value < vr.value
        WHEN e.operator LIKE '>' THEN vl.value > vr.value
        ELSE vl.value = vr.value
        END AS value
FROM variables AS vl, variables AS vr, expressions AS e
WHERE vl.name = e.left_operand AND vr.name = e.right_operand;