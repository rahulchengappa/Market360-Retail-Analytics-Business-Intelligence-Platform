\copy stg_customers FROM 'D:/Market360/data/customers.csv' DELIMITER ',' CSV HEADER;
\copy stg_products FROM 'D:/Market360/data/products.csv' DELIMITER ',' CSV HEADER;
\copy stg_stores FROM 'D:/Market360/data/stores.csv' DELIMITER ',' CSV HEADER;
\copy stg_orders FROM 'D:/Market360/data/orders.csv' DELIMITER ',' CSV HEADER;
\copy stg_order_items FROM 'D:/Market360/data/order_items.csv' DELIMITER ',' CSV HEADER;
\copy stg_inventory FROM 'D:/Market360/data/inventory.csv' DELIMITER ',' CSV HEADER;