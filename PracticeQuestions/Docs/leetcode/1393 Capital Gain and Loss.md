<h1>
    <a href = "https://leetcode.com/problems/capital-gainloss/description/">
        1393
    </a>
    : Capital Gain/Loss</h1>

# Intuition

This problem requires calculating the capital gain or loss for each stock by summing up the prices of 'Buy' and 'Sell' transactions separately and then computing their difference. Since selling price minus buying price determines the gain or loss, we need to aggregate these values for each stock.

# Approach

1. **Filter and Aggregate:**
    - Use `SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END)` to compute the total selling price per stock.
    - Use `SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END)` to compute the total buying price per stock.
2. **Calculate Gain/Loss:**
    - Subtract the total buying price from the total selling price for each stock.
3. **Group by Stock Name:**
    - Ensure calculations are performed separately for each unique `stock_name`.
4. **Final Selection:**
    - Display `stock_name` and the computed capital gain/loss.

# Complexity

-   **Time complexity:**
    -   Since we scan all rows in the table and aggregate them using `GROUP BY`, the worst-case complexity is $$O(n)$$, where _n_ is the number of records in the `Stocks` table.
-   **Space complexity:**
    -   The query uses only a fixed amount of extra space for aggregations, resulting in $$O(1)$$ additional space usage.

# Code

```mysql
# Write your MySQL query statement below
SELECT
    stock_name,
    _sold - _bought AS capital_gain_loss
FROM
    (
        SELECT
            stock_name,
            SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) AS _sold,
            SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) AS _bought
        FROM
            Stocks
        GROUP BY
            stock_name
    ) s;
```

<br>
<hr>

# Alternative Solution

Another approach to solving this problem is using conditional aggregation in a single query without subqueries:

```mysql
SELECT
    stock_name,
    SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) -
    SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) AS capital_gain_loss
FROM
    Stocks
GROUP BY
    stock_name;
```

### Explanation:

-   Instead of using a subquery, we directly compute the total selling and buying prices within the main query.
-   This makes the query more concise and potentially more efficient by reducing the need for an additional derived table.
-   The final result remains the same, calculating the net gain or loss for each stock.
