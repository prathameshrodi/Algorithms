SELECT column_name
FROM table_name
ORDER BY column_name DESC
LIMIT 1 OFFSET 4;

To select only the 5th highest value, you can use the `OFFSET` clause with `LIMIT` or subqueries, depending on your SQL flavor.

### Query Using `OFFSET`
```sql
SELECT column_name
FROM table_name
ORDER BY column_name DESC
LIMIT 1 OFFSET 4;
```

### Explanation:
- `ORDER BY column_name DESC`: Orders the results in descending order.
- `LIMIT 1`: Selects only one row.
- `OFFSET 4`: Skips the first 4 rows to get the 5th row.

### Example Query:
```sql
SELECT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 4;
```

### Alternative Using Subquery
```sql
SELECT MIN(column_name) AS fifth_highest
FROM (
    SELECT column_name
    FROM table_name
    ORDER BY column_name DESC
    LIMIT 5
) AS top_five;
```

This approach works for databases that don't support `OFFSET`.