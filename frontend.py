# frontend.py
import streamlit as st
import pandas as pd
from data_loader import load_health_data
from detection import detect_outbreaks
from risk_model import model_risk
from alerts import generate_alerts
from recommender import suggest_interventions

st.set_page_config(page_title="Health Outbreak Monitor", layout="wide")
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
        }
        .alert-box {
            background-color: #fff5f5;
            border-left: 6px solid #e74c3c;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 12px;
        }
        .success-box {
            background-color: #e8f5e9;
            border-left: 6px solid #2ecc71;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
        }
        .css-1v0mbdj {
            background-color: #ffffff !important;
        }
    </style>
""", unsafe_allow_html=True)


st.title("🩺 Community Health Outbreak Monitor")

st.markdown("Upload health surveillance data below to detect early signs of potential outbreaks.")

uploaded_file = st.file_uploader("📤 Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["date"] = pd.to_datetime(df["date"])
    st.subheader("📋 Preview of Uploaded Data")
    st.dataframe(df, use_container_width=True)

    with st.spinner("🧠 Running analysis..."):
        outbreak_df = detect_outbreaks(df)
        risk_df = model_risk(outbreak_df)
        alerts = generate_alerts(risk_df)
        recommendations = suggest_interventions(alerts)

    st.subheader("📈 Trends by Region")
    for region in df["region"].unique():
        st.markdown(f"**Region:** {region}")
        region_data = df[df["region"] == region].sort_values("date")
        st.line_chart(region_data.set_index("date")[["cases"]])

    st.subheader("🚨 Alerts & Recommendations")
    if alerts:
        for alert, reco in zip(alerts, recommendations):
            st.markdown(f"""
                <div class="alert-box">
                    <strong>📍 Region:</strong> {alert['region']}<br>
                    <strong>📅 Date:</strong> {alert['date']}<br>
                    <strong>⚠️ Alert Level:</strong> <span style="color:red">{alert['alert_level']}</span><br>
                    <strong>💡 Recommendation:</strong> {reco}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="success-box">
                ✅ No outbreaks detected. Community health is stable.
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("Please upload a CSV file with fields: `region`, `date`, `symptom`, `cases`.")

