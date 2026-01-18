import pandas as pd


def main():
    stat = pd.read_csv("outputs/anomalies/statistical_anomalies.csv")
    ml = pd.read_csv("outputs/anomalies/ml_anomalies.csv")

    key_cols = ["year_month", "state", "district"]

    stat["stat"] = 1
    ml["ml"] = 1

    merged = pd.merge(
        stat[key_cols + ["stat"]],
        ml[key_cols + ["ml"]],
        on=key_cols,
        how="outer"
    ).fillna(0)

    print("\n=== ANOMALY OVERLAP SUMMARY ===")
    print(merged[["stat", "ml"]].value_counts())

    merged.to_csv(
        "outputs/anomalies/anomaly_overlap.csv",
        index=False
    )


if __name__ == "__main__":
    main()
