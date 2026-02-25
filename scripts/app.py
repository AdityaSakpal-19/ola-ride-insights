import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="OLA Ride Insights",
    page_icon="🚖",
    layout="wide"
)

st.title("🚖 OLA Ride Data Dashboard")
st.markdown("Interactive ride analytics using SQL + Streamlit")

# -------------------------------
# DATABASE CONNECTION (SQLite)
# -------------------------------
engine = create_engine("sqlite:///ola_rides.db")

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    query = "SELECT * FROM OLA_RIDES"
    return pd.read_sql(query, engine)

df = load_data()

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔎 Filters")

vehicle_types = ["All"] + sorted(df["vehicle_type"].dropna().unique().tolist())
payment_methods = ["All"] + sorted(df["payment_method"].dropna().unique().tolist())
booking_status = ["All"] + sorted(df["booking_status"].dropna().unique().tolist())

selected_vehicle = st.sidebar.selectbox("Vehicle Type", vehicle_types)
selected_payment = st.sidebar.selectbox("Payment Method", payment_methods)
selected_status = st.sidebar.selectbox("Booking Status", booking_status)

# Apply Filters
filtered_df = df.copy()

if selected_vehicle != "All":
    filtered_df = filtered_df[filtered_df["vehicle_type"] == selected_vehicle]

if selected_payment != "All":
    filtered_df = filtered_df[filtered_df["payment_method"] == selected_payment]

if selected_status != "All":
    filtered_df = filtered_df[filtered_df["booking_status"] == selected_status]

# -------------------------------
# KPI SECTION
# -------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(filtered_df))
col2.metric("Total Revenue", f"₹ {filtered_df['booking_value'].sum():,.0f}")
col3.metric("Avg Distance (km)", f"{filtered_df['ride_distance'].mean():.2f}")
col4.metric("Avg Customer Rating", f"{filtered_df['customer_rating'].mean():.2f}")

# -------------------------------
# CHARTS
# -------------------------------
st.subheader("📈 Booking Status Breakdown")

status_data = (
    filtered_df.groupby("booking_status")
    .size()
    .reset_index(name="count")
)

st.bar_chart(status_data.set_index("booking_status"))

st.subheader("💳 Payment Method Distribution")

payment_data = (
    filtered_df.groupby("payment_method")
    .size()
    .reset_index(name="count")
)

st.bar_chart(payment_data.set_index("payment_method"))

st.subheader("🚗 Revenue by Vehicle Type")

revenue_data = (
    filtered_df.groupby("vehicle_type")["booking_value"]
    .sum()
    .reset_index()
)

st.bar_chart(revenue_data.set_index("vehicle_type"))

# -------------------------------
# DATA TABLE
# -------------------------------
st.subheader("📋 Ride Data (Preview)")
st.dataframe(filtered_df.head(200))

st.markdown("---")
st.caption("Built using Python, SQLite, and Streamlit")