-- STAGING TABLES

CREATE TABLE stg_customers (
    customer_id INT,
    first_name TEXT,
    last_name TEXT,
    city TEXT,
    state TEXT
);

CREATE TABLE stg_products (
    product_id INT,
    product_name TEXT,
    category TEXT,
    cost_price NUMERIC,
    selling_price NUMERIC
);

CREATE TABLE stg_stores (
    store_id INT,
    store_name TEXT,
    city TEXT,
    region TEXT
);

CREATE TABLE stg_orders (
    order_id INT,
    order_date DATE,
    customer_id INT,
    store_id INT
);

CREATE TABLE stg_order_items (
    order_item_id INT,
    order_id INT,
    product_id INT,
    quantity INT,
    revenue NUMERIC
);

CREATE TABLE stg_inventory (
    inventory_id INT,
    store_id INT,
    product_id INT,
    stock_quantity INT
);