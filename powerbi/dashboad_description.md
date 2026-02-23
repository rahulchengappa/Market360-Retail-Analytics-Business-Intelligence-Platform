📊 Market360 – Retail Analytics Dashboard

1️⃣ Dashboard Objective

The Retail Analytics Dashboard provides an executive-level overview of financial performance, growth trends, regional contribution, and product-level revenue distribution.

It enables business stakeholders to:

- Monitor revenue and profitability

- Track growth performance over time

- Identify high-performing regions

- Analyze product-level revenue contribution

- Detect volatility patterns in sales growth

2️⃣ Dashboard Layout Overview

🔵 Executive KPI Section (Top Layer)

The dashboard starts with four key performance indicators:

- Total Revenue

- Total Profit

- Profit Margin %

- Year-over-Year (YoY) Growth %

Purpose:
Provides a quick financial health snapshot for leadership.

🔵 Time-Based Performance Analysis

- Total Revenue & Total Profit by YearMonth

- Combo chart (Column + Line)

- Columns → Revenue

- Line → Profit

Insight:

- Tracks revenue trend and profit stability over time.

- Total Revenue by YearMonth

- Horizontal bar chart

- Monthly revenue comparison

Insight:
Highlights peak-performing and weak months.

**MoM Growth % by YearMonth**

- Line chart

- Shows volatility and growth fluctuations

Insight:
Detects abnormal growth spikes and seasonal patterns.

🔵 Regional & Product Analysis

**Total Revenue by Region**

- Column chart

- Compares North, East, South, West

Insight:
Identifies top-performing geographical regions.

**Total Revenue by Product**

- Donut chart

- Revenue contribution by product_id

Insight:
Highlights revenue concentration and product dominance.

3️⃣ Interactive Filters

The dashboard includes slicers for:

- Year Filter

- Region Filter

- Category Filter

These allow dynamic drill-down and comparative analysis.

4️⃣ Key Business Insights

From the dashboard:

- Revenue and profit move strongly together.

- Growth shows volatility in certain months.

- Revenue is regionally concentrated.

- Product revenue distribution indicates moderate concentration risk.

- Margin is consistently high (72%+), indicating strong pricing strategy.

5️⃣ Data Model

The dashboard is powered by a PostgreSQL star schema:

- Fact Tables:

- fact_sales

- fact_inventory

Dimension Tables:

- dim_date

- dim_products

- dim_customers

- dim_stores