import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Caffeine Intake Dashboard", layout="wide")
st.title("☕ Caffeine Intake Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_caffeine_data.csv")

df = load_data()

# Sidebar filter
st.sidebar.header("Filter Data")
gender = st.sidebar.selectbox("Select Gender", ["All", "Male", "Female"])
if gender != "All":
    col = "gender_male" if gender == "Male" else "gender_female"
    df = df[df[col] == 1]

# Key metrics
st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Focus", f"{df['focus_level'].mean():.2f}")
col2.metric("Avg Sleep", f"{df['sleep_quality'].mean():.2f}")
col3.metric("Sleep Impacted", f"{df['sleep_impacted'].mean()*100:.1f}%")

# Helper plot function
def plot(title, x, y):
    st.markdown(f"### {title}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x, y=y, ax=ax)
    st.pyplot(fig)

# Charts
plot("Caffeine vs Sleep Quality", "caffeine_mg", "sleep_quality")
plot("Caffeine vs Focus Level", "caffeine_mg", "focus_level")

# Bar charts
def barplot(title, labels, values):
    st.markdown(f"### {title}")
    fig, ax = plt.subplots()
    sns.barplot(x=labels, y=values, ax=ax)
    st.pyplot(fig)

barplot("Beverage Preferences", ["Coffee", "Energy Drink", "Tea"], [
    df["beverage_coffee"].sum(),
    df["beverage_energy_drink"].sum(),
    df["beverage_tea"].sum()
])

barplot("Time of Day Consumption", ["Morning", "Afternoon", "Evening"], [
    df["time_of_day_morning"].sum(),
    df["time_of_day_afternoon"].sum(),
    df["time_of_day_evening"].sum()
])

