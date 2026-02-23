import pandas as pd

# -------------------------
# LOAD DATA
# -------------------------
customers = pd.read_csv("customers.csv", parse_dates=["join_date"])
products = pd.read_csv("products.csv")
stores = pd.read_csv("stores.csv")
orders = pd.read_csv("orders.csv", parse_dates=["order_date"])
order_items = pd.read_csv("order_items.csv")
inventory = pd.read_csv("inventory.csv")

print("✅ Data loaded successfully")

# -------------------------
# MERGE ORDER DATA
# -------------------------
order_details = order_items.merge(products, on="product_id")
order_details = order_details.merge(orders, on="order_id")
order_details["profit"] = order_details["revenue"] - (order_details["quantity"] * order_details["cost"])

print("✅ Order details merged")

# -------------------------
# KPI TABLE 1 — SALES SUMMARY
# -------------------------
sales_summary = order_details.groupby("order_date").agg(
    total_revenue=("revenue", "sum"),
    total_profit=("profit", "sum"),
    total_orders=("order_id", "nunique")
).reset_index()

sales_summary["profit_margin"] = (
    sales_summary["total_profit"] / sales_summary["total_revenue"]
)

sales_summary.to_csv("sales_summary.csv", index=False)
print("✅ Sales summary created")

# -------------------------
# KPI TABLE 2 — CUSTOMER SUMMARY
# -------------------------
customer_orders = orders.groupby("customer_id").agg(
    total_orders=("order_id", "nunique")
).reset_index()

customer_summary = customers.merge(customer_orders, on="customer_id", how="left")
customer_summary["total_orders"] = customer_summary["total_orders"].fillna(0)

customer_summary.to_csv("customer_summary.csv", index=False)
print("✅ Customer summary created")

# -------------------------
# KPI TABLE 3 — INVENTORY STATUS
# -------------------------
inventory_status = inventory.copy()
inventory_status["stock_status"] = inventory_status.apply(
    lambda x: "Stock-out" if x["stock_level"] == 0
    else "Low Stock" if x["stock_level"] < x["reorder_point"]
    else "Healthy",
    axis=1
)

inventory_status.to_csv("inventory_status.csv", index=False)
print("✅ Inventory status created")

print("🚀 Market360 ETL pipeline completed successfully!")
