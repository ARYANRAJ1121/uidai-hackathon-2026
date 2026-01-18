import pandas as pd
import os

from src.anomaly_detection import (
    detect_statistical_anomalies,
    detect_ml_anomalies,
)


def main():
    df = pd.read_csv("data/processed/monthly_features.csv")

    os.makedirs("outputs/anomalies", exist_ok=True)

    stat_anoms = detect_statistical_anomalies(df)
    ml_anoms = detect_ml_anomalies(df)

    stat_anoms.to_csv(
        "outputs/anomalies/statistical_anomalies.csv",
        index=False
    )
    ml_anoms.to_csv(
        "outputs/anomalies/ml_anomalies.csv",
        index=False
    )

    print("=== ANOMALY DETECTION COMPLETE ===")
    print(f"Statistical anomalies: {len(stat_anoms)}")
    print(f"ML anomalies: {len(ml_anoms)}")


if __name__ == "__main__":
    main()
