from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="California Housing Data",
    layout="wide",
)

# 读取与本程序放在同一文件夹的 CSV。
csv_path = Path(__file__).parent / "housing.csv"
df = pd.read_csv(csv_path)

st.title("California Housing Data (1990) by Wang Yanxi")

# 房价筛选。
min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000,
)

st.subheader("See more filters in the sidebar:")

# 侧边栏：默认选中全部位置类型。
location_types = [
    "NEAR BAY",
    "<1H OCEAN",
    "INLAND",
    "NEAR OCEAN",
    "ISLAND",
]

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types,
)

# 侧边栏：收入等级。
income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"],
)

# 同时应用房价和位置筛选。
filtered_df = df[
    (df["median_house_value"] >= min_value)
    & (df["ocean_proximity"].isin(selected_locations))
]

# 按要求使用 if 语句筛选收入。
if income_level == "Low":
    filtered_df = filtered_df[
        filtered_df["median_income"] <= 2.5
    ]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5)
        & (filtered_df["median_income"] < 4.5)
    ]
else:
    filtered_df = filtered_df[
        filtered_df["median_income"] >= 4.5
    ]

# 地图和直方图均使用同一份筛选结果。
if filtered_df.empty:
    st.info("没有符合条件的地区，请调整筛选条件。")
else:
    st.map(filtered_df[["latitude", "longitude"]])

    fig, ax = plt.subplots()
    ax.hist(
        filtered_df["median_house_value"],
        bins=30,
        edgecolor="white",
    )
    ax.set_xlabel("Median House Value (USD)")
    ax.set_ylabel("Number of Districts")
    ax.set_title("Distribution of Median House Value")

    st.pyplot(fig)
    plt.close(fig)