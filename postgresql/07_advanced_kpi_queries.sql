//mom growth //
WITH monthly_sales AS (
    SELECT
        d.year,
        d.month,
        SUM(f.revenue) AS total_revenue
    FROM fact_sales f
    JOIN dim_date d ON f.order_date = d.full_date
    GROUP BY d.year, d.month
)
SELECT *,
    (total_revenue - LAG(total_revenue) OVER (ORDER BY year, month))
    / LAG(total_revenue) OVER (ORDER BY year, month) AS mom_growth
FROM monthly_sales;


//profit margin //
SELECT
    SUM(f.revenue) AS total_revenue,
    SUM(f.revenue - (f.quantity * p.cost_price)) AS total_profit,
    (SUM(f.revenue - (f.quantity * p.cost_price)) / SUM(f.revenue)) * 100 AS profit_margin
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id;


//customer rfm//
SELECT
    customer_id,
    SUM(revenue) AS total_spent,
    COUNT(order_id) AS frequency,
    MAX(order_date) AS last_purchase
FROM fact_sales
GROUP BY customer_id;