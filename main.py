from data_loader import load_health_data
from detection import detect_outbreaks
from risk_model import model_risk
from alerts import generate_alerts
from recommender import suggest_interventions

def run_system():
    print("Loading health data...")
    df = load_health_data("sample_data.csv")

    print("Detecting outbreaks...")
    outbreak_df = detect_outbreaks(df)

    print("Modeling risk levels...")

    risk_df = model_risk(outbreak_df)

    print("Generating alerts...")
    alerts = generate_alerts(risk_df)

    print("Suggesting interventions...")
    recommendations = suggest_interventions(alerts)

    if alerts:
        for alert, reco in zip(alerts, recommendations):
            print("--- ALERT ---")
            print(f"Region: {alert['region']} | Date: {alert['date']} | Level: {alert['alert_level']}")
            print(f"Recommendation: {reco}")
    else:
        print("✅ No outbreaks detected. Community health is stable.")



if __name__ == "__main__":
    run_system()