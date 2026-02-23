📊 Market360 – Retail Analytics Data Platform
🔹 Project Overview

Market360 is an end-to-end retail analytics solution built during internship to simulate a real-world enterprise data pipeline. The system integrates:

- Data generation (Python)
- ETL pipeline
- PostgreSQL data warehouse (star schema)
- Power BI dashboard
- Advanced analytics layer (Python ML)

🔹 Architecture

Layer 1 – Data Generation

- Synthetic retail dataset (customers, orders, products, stores)

- Generated using Python (Faker, Pandas)

Layer 2 – ETL Pipeline

- Data cleaning and transformation

- Fact and dimension tables created

- Loaded into PostgreSQL

Layer 3 – Data Warehouse

- Star schema design

- fact_sales

- dim_date

- dim_products

- dim_customers

- dim_stores

Layer 4 – BI Dashboard

- KPI layer:

Total Revenue

Total Profit

Profit Margin %

YoY Growth %

Trend analysis

MoM growth

Region breakdown

Product performance

Layer 5 – Advanced Analytics (Python)

- Rolling average smoothing

- Correlation analysis

- Volatility measurement

- Z-score anomaly detection

- Customer segmentation (K-Means clustering using RFM model)

🔹 Key Insights

- Revenue and Profit show near-linear correlation (0.9994)

- MoM volatility = 0.3464 (moderate growth fluctuation)

- March 2024 identified as anomaly (z-score > 4)

- Customer segmentation identified:

- High-value customers

- Mid-tier customers

- Low-value customers

- Dormant/churned customers

🔹 Tech Stack

- Python (Pandas, Matplotlib, Seaborn, Scikit-learn)

- PostgreSQL

- SQLAlchemy

- Power BI

- Star Schema Modeling