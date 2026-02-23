import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

# -------------------------
# CONFIG
# -------------------------
NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 120
NUM_STORES = 20
NUM_ORDERS = 5000

REGIONS = ["North", "South", "East", "West"]
CATEGORIES = ["Electronics", "Apparel", "Home", "Beauty", "Sports"]
STORE_TYPES = ["Online", "Offline"]
SEGMENTS = ["Regular", "Premium"]

# -------------------------
# CUSTOMERS
# -------------------------
customers = []
for i in range(NUM_CUSTOMERS):
    customers.append({
        "customer_id": f"CUST{i+1:05d}",
        "join_date": fake.date_between(start_date="-3y", end_date="today"),
        "region": random.choice(REGIONS),
        "segment": random.choice(SEGMENTS)
    })

customers_df = pd.DataFrame(customers)

# -------------------------
# PRODUCTS
# -------------------------
products = []
for i in range(NUM_PRODUCTS):
    price = round(random.uniform(10, 500), 2)
    cost = round(price * random.uniform(0.5, 0.75), 2)
    products.append({
        "product_id": f"PROD{i+1:04d}",
        "category": random.choice(CATEGORIES),
        "price": price,
        "cost": cost
    })

products_df = pd.DataFrame(products)

# -------------------------
# STORES
# -------------------------
stores = []
for i in range(NUM_STORES):
    stores.append({
        "store_id": f"STORE{i+1:03d}",
        "region": random.choice(REGIONS),
        "store_type": random.choice(STORE_TYPES)
    })

stores_df = pd.DataFrame(stores)

# -------------------------
# ORDERS
# -------------------------
orders = []
for i in range(NUM_ORDERS):
    orders.append({
        "order_id": f"ORD{i+1:06d}",
        "customer_id": random.choice(customers_df["customer_id"]),
        "store_id": random.choice(stores_df["store_id"]),
        "order_date": fake.date_between(start_date="-2y", end_date="today")
    })

orders_df = pd.DataFrame(orders)

# -------------------------
# ORDER ITEMS
# -------------------------
order_items = []
for order in orders_df.itertuples():
    num_items = random.randint(1, 4)
    products_sample = products_df.sample(num_items)

    for _, product in products_sample.iterrows():
        quantity = random.randint(1, 5)
        revenue = round(quantity * product["price"], 2)
        order_items.append({
            "order_id": order.order_id,
            "product_id": product["product_id"],
            "quantity": quantity,
            "revenue": revenue
        })

order_items_df = pd.DataFrame(order_items)

# -------------------------
# INVENTORY
# -------------------------
inventory = []
for _, product in products_df.iterrows():
    for _, store in stores_df.iterrows():
        inventory.append({
            "product_id": product["product_id"],
            "store_id": store["store_id"],
            "stock_level": random.randint(0, 500),
            "reorder_point": random.randint(30, 100)
        })

inventory_df = pd.DataFrame(inventory)

# -------------------------
# SAVE FILES
# -------------------------
customers_df.to_csv("customers.csv", index=False)
products_df.to_csv("products.csv", index=False)
stores_df.to_csv("stores.csv", index=False)
orders_df.to_csv("orders.csv", index=False)
order_items_df.to_csv("order_items.csv", index=False)
inventory_df.to_csv("inventory.csv", index=False)

print("✅ Market360 retail datasets generated successfully!")
