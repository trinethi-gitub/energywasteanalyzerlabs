import streamlit as st
import pandas as pd
import plotly.express as px

from utils.calculations import calculate_energy

st.set_page_config(
    page_title="Energy Waste Analyzer",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Energy Waste Analyzer for Laboratories")

st.markdown("### Enter Laboratory Details")

col1, col2 = st.columns(2)

with col1:

    computers = st.number_input(
        "Number of Computers",
        min_value=0,
        value=20
    )

    fans = st.number_input(
        "Number of Fans",
        min_value=0,
        value=8
    )

    lights = st.number_input(
        "Number of Lights",
        min_value=0,
        value=10
    )

with col2:

    computer_power = st.number_input(
        "Computer Power (Watts)",
        value=100
    )

    fan_power = st.number_input(
        "Fan Power (Watts)",
        value=75
    )

    light_power = st.number_input(
        "Light Power (Watts)",
        value=20
    )

hours = st.slider(
    "Extra Running Time (Hours)",
    1,
    12,
    2
)

cost = st.number_input(
    "Electricity Cost per Unit (₹)",
    value=8
)

if st.button("Calculate Energy Waste"):

    result = calculate_energy(
        computers,
        fans,
        lights,
        computer_power,
        fan_power,
        light_power,
        hours,
        cost
    )

    st.success("Calculation Completed")

    st.metric(
        "Total Energy Wasted (kWh)",
        round(result["total_energy"], 2)
    )

    st.metric(
        "Estimated Cost",
        f"₹ {round(result['total_cost'],2)}"
    )

    df = pd.DataFrame({
        "Device": ["Computers", "Fans", "Lights"],
        "Energy (kWh)": [
            result["computer_energy"],
            result["fan_energy"],
            result["light_energy"]
        ]
    })

    st.subheader("Energy Consumption")

    fig = px.bar(
        df,
        x="Device",
        y="Energy (kWh)",
        color="Device",
        text="Energy (kWh)"
    )

    st.plotly_chart(fig, use_container_width=True)

    pie = px.pie(
        df,
        values="Energy (kWh)",
        names="Device",
        title="Energy Distribution"
    )

    st.plotly_chart(pie, use_container_width=True)

    st.subheader("Suggestions")

    st.write("✅ Turn OFF computers after lab hours.")
    st.write("✅ Switch OFF lights when not required.")
    st.write("✅ Turn OFF fans in empty rooms.")
    st.write("✅ Use LED lighting.")
    st.write("✅ Conduct regular energy audits.")