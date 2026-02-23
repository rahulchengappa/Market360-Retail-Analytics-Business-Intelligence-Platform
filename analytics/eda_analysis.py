import pandas as pd
from sqlalchemy import create_engine
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# PostgreSQL connection
engine = create_engine("postgresql://postgres:yourownpassword@localhost:5432/market360")

# Query monthly revenue & profit
query = """
SELECT 
    d.year,
    d.month,
    SUM(f.revenue) AS total_revenue,
    SUM(f.revenue - (f.quantity * p.cost_price)) AS total_profit
FROM public.fact_sales f
JOIN public.dim_date d ON f.order_date = d.full_date
JOIN public.dim_products p ON f.product_id = p.product_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
"""

df = pd.read_sql(query, engine)

print(df.head())

# Rolling Average
df['rolling_revenue'] = df['total_revenue'].rolling(window=3).mean()

plt.figure()
plt.plot(df['total_revenue'])
plt.plot(df['rolling_revenue'])
plt.title("Revenue vs Rolling Average")  

# Correlation Analysis
correlation = df['total_revenue'].corr(df['total_profit'])
print("\nRevenue-Profit Correlation:", round(correlation, 4))

plt.figure()
sns.scatterplot(x=df['total_revenue'], y=df['total_profit'])
plt.title("Revenue vs Profit Relationship")
plt.xlabel("Revenue")
plt.ylabel("Profit")


# Volatility Analysis
df['mom_growth'] = df['total_revenue'].pct_change()

volatility = df['mom_growth'].std()
print("MoM Growth Volatility (Std Dev):", round(volatility, 4))

plt.figure()
sns.histplot(df['mom_growth'].dropna(), kde=True)
plt.title("Distribution of MoM Growth")


# Z-score anomaly detection
df['z_score'] = (df['mom_growth'] - df['mom_growth'].mean()) / df['mom_growth'].std()

anomalies = df[abs(df['z_score']) > 2]

print("\nAnomalies detected:")
print(anomalies[['year','month','mom_growth','z_score']])


# -----------------------------
# CUSTOMER SEGMENTATION
# -----------------------------

customer_query = """
SELECT 
    customer_id,
    SUM(revenue) AS total_spent,
    COUNT(order_id) AS frequency,
    MAX(order_date) AS last_purchase
FROM public.fact_sales
GROUP BY customer_id;
"""

cust_df = pd.read_sql(customer_query, engine)

cust_df['last_purchase'] = pd.to_datetime(cust_df['last_purchase'])
cust_df['recency'] = (cust_df['last_purchase'].max() - cust_df['last_purchase']).dt.days

rfm = cust_df[['total_spent', 'frequency', 'recency']]

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

kmeans = KMeans(n_clusters=4, random_state=42)
cust_df['segment'] = kmeans.fit_predict(rfm_scaled)

print("\nCustomer Segmentation Summary:")
print(cust_df.groupby('segment')[['total_spent','frequency','recency']].mean())

plt.figure()
sns.scatterplot(
    x=cust_df['total_spent'],
    y=cust_df['frequency'],
    hue=cust_df['segment'],
    palette='viridis'
)
plt.title("Customer Segments (Spend vs Frequency)")

plt.show()
input("Press Enter to exit...")