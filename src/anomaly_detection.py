import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest


def detect_statistical_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["stat_anomaly"] = (
        (df["z_demo_update_rate"].abs() > 3) |
        (df["z_bio_update_rate"].abs() > 3) |
        (df["update_imbalance"].abs() > 0.7)
    )

    return df[df["stat_anomaly"]]


def detect_ml_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    features = df[
        [
            "demo_update_rate",
            "bio_update_rate",
            "update_imbalance",
            "demo_mom_delta",
            "bio_mom_delta",
        ]
    ].fillna(0)

    model = IsolationForest(
        n_estimators=200,
        contamination=0.02,
        random_state=42
    )

    df["ml_anomaly_score"] = model.fit_predict(features)
    return df[df["ml_anomaly_score"] == -1]
