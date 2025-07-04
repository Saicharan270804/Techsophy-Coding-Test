def generate_alerts(df):
    """
    Create alert messages from risk data.
    Returns a list of alert dicts.
    """
    alerts = []

    for _, row in df.iterrows():
        alert = {
            "region": row["region"],
            "date": row["date"].strftime("%Y-%m-%d"),
            "alert_level": row["risk_level"]
        }
        alerts.append(alert)

    return alerts
