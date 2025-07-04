def model_risk(df):
    """
    Assign risk levels based on case count and z-score.
    """
    def assign_risk(row):
        if row['cases'] > 100 or row['z_score'] > 5:
            return "High"
        elif row['cases'] > 50 or row['z_score'] > 3:
            return "Medium"
        else:
            return "Low"
    
    df = df.copy()
    df['risk_level'] = df.apply(assign_risk, axis=1)
    return df
