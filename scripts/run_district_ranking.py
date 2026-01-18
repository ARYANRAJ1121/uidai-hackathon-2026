import pandas as pd


def main():
    df = pd.read_csv(
        "outputs/anomalies/post_stabilization_anomalies.csv"
    )

    # 1. District-level anomaly frequency
    ranking = (
        df.groupby(["state", "district"])
        .agg(
            anomaly_months=("year_month", "nunique"),
            stat_count=("stat", "sum"),
            ml_count=("ml", "sum"),
        )
        .reset_index()
        .sort_values("anomaly_months", ascending=False)
    )

    ranking.to_csv(
        "outputs/anomalies/district_anomaly_ranking.csv",
        index=False
    )

    # 2. High-confidence anomalies (stat + ML overlap)
    high_conf = df[(df["stat"] == 1) & (df["ml"] == 1)]

    high_conf.to_csv(
        "outputs/anomalies/high_confidence_anomalies.csv",
        index=False
    )

    print("=== DISTRICT RANKING COMPLETE ===")
    print("Top 10 districts by anomaly persistence:")
    print(ranking.head(10))


if __name__ == "__main__":
    main()
