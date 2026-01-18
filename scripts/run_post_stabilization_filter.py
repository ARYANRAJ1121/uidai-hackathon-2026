import pandas as pd
import os


def main():
    df = pd.read_csv("outputs/anomalies/anomaly_overlap.csv")

    post = df[df["year_month"] >= "2025-03"]

    os.makedirs("outputs/anomalies", exist_ok=True)

    post.to_csv(
        "outputs/anomalies/post_stabilization_anomalies.csv",
        index=False
    )

    print("=== POST-STABILIZATION FILTER APPLIED ===")
    print(f"Remaining anomalies: {len(post)}")


if __name__ == "__main__":
    main()
