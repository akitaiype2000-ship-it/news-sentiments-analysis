import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database connection using SQLAlchemy
engine = create_engine(
    "postgresql+psycopg2://postgres:NewsProject123!@news-sentiment-db.cj0mi2u8yzvv.ap-south-1.rds.amazonaws.com:5432/postgres"
)

# Read data from PostgreSQL
query = "SELECT * FROM news;"
df = pd.read_sql(query, engine)

# Streamlit page settings
st.set_page_config(
    page_title="News Sentiment Dashboard",
    layout="wide"
)

# Dashboard title
st.title("📰 News Sentiment Dashboard")

# Display data
st.subheader("News Data")
st.dataframe(df)

# Display sentiment distribution
if "sentiment" in df.columns:
    st.subheader("Sentiment Distribution")
    sentiment_counts = df["sentiment"].value_counts()
    st.bar_chart(sentiment_counts)

# Dispose of the SQLAlchemy engine
engine.dispose()