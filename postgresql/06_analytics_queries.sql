//monthly revenue//
SELECT
    d.year,
    d.month,
    SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_date d ON f.order_date = d.full_date
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

//revenue by region//
SELECT
    s.region,
    SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_stores s ON f.store_id = s.store_id
GROUP BY s.region
ORDER BY total_revenue DESC;

//top 10 products//
SELECT
    p.product_name,
    SUM(f.revenue) AS total_revenue
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 10;

//inventory risk analysis//
SELECT
    p.product_name,
    SUM(i.stock_quantity) AS total_stock,
    SUM(f.quantity) AS total_quantity_sold
FROM fact_sales f
JOIN fact_inventory i ON f.product_id = i.product_id
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.product_name;
