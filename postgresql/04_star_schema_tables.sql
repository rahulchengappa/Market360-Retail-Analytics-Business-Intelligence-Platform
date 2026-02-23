-- DIMENSION TABLES

CREATE TABLE dim_customers AS
SELECT DISTINCT customer_id, first_name, last_name, city, state
FROM stg_customers;

CREATE TABLE dim_products AS
SELECT DISTINCT product_id, product_name, category, cost_price, selling_price
FROM stg_products;

CREATE TABLE dim_stores AS
SELECT DISTINCT store_id, store_name, city, region
FROM stg_stores;

CREATE TABLE dim_date AS
SELECT DISTINCT
    order_date AS full_date,
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month
FROM stg_orders;

-- FACT TABLES

CREATE TABLE fact_sales AS
SELECT
    oi.order_id,
    o.order_date,
    o.customer_id,
    o.store_id,
    oi.product_id,
    oi.quantity,
    oi.revenue
FROM stg_order_items oi
JOIN stg_orders o ON oi.order_id = o.order_id;

CREATE TABLE fact_inventory AS
SELECT
    store_id,
    product_id,
    stock_quantity
FROM stg_inventory;