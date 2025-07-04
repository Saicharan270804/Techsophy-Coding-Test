def suggest_interventions(alerts):
    """
    Recommend public health interventions based on alert level.
    """
    recommendations = []

    for alert in alerts:
        level = alert["alert_level"]
        if level == "High":
            reco = "Deploy mobile testing units and restrict public gatherings."
        elif level == "Medium":
            reco = "Increase health surveillance and promote mask usage."
        else:
            reco = "Continue routine monitoring and public hygiene campaigns."
        
        recommendations.append(reco)

    return recommendations
