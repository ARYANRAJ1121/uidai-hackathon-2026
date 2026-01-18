import os
import pandas as pd
import matplotlib.pyplot as plt


OUTPUT_DIR = "outputs/figures"


def plot_monthly_anomaly_trend():
    df = pd.read_csv("outputs/anomalies/anomaly_overlap.csv")

    monthly = (
        df.groupby("year_month")[["stat", "ml"]]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))
    plt.plot(monthly.index, monthly["stat"], marker="o", label="Statistical Anomalies")
    plt.plot(monthly.index, monthly["ml"], marker="o", label="ML Anomalies")

    plt.title("Monthly Anomaly Volume (Statistical vs ML)")
    plt.xlabel("Year–Month")
    plt.ylabel("Number of Anomalies")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "monthly_anomaly_trend.png"))
    plt.close()


def plot_top_districts():
    ranking = pd.read_csv(
        "outputs/anomalies/district_anomaly_ranking.csv"
    ).head(10)

    plt.figure(figsize=(10, 5))
    plt.bar(
        ranking["district"],
        ranking["anomaly_months"]
    )

    plt.title("Top Districts by Persistent Anomalies (Post-Stabilization)")
    plt.xlabel("District")
    plt.ylabel("Number of Anomalous Months")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "top_districts.png"))
    plt.close()


def plot_kollam_case_study():
    features = pd.read_csv("data/processed/monthly_features.csv")

    kollam = features[
        (features["state"] == "Kerala") &
        (features["district"] == "Kollam")
    ].sort_values("year_month")

    if kollam.empty:
        print("⚠️ Kollam data not found — skipping case study plot.")
        return

    plt.figure(figsize=(10, 5))

    plt.plot(
        kollam["year_month"],
        kollam["demo_update_rate"],
        marker="o",
        label="Demographic Update Rate"
    )

    plt.plot(
        kollam["year_month"],
        kollam["bio_update_rate"],
        marker="o",
        label="Biometric Update Rate"
    )

    if "2025-04" in kollam["year_month"].values:
        plt.axvline(
            x="2025-04",
            color="red",
            linestyle="--",
            label="High-Confidence Anomaly (Apr 2025)"
        )

    plt.title("Case Study: Kollam District, Kerala")
    plt.xlabel("Year–Month")
    plt.ylabel("Update Rate")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "kollam_case_study.png"))
    plt.close()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Generating judge-ready visualizations...")

    plot_monthly_anomaly_trend()
    plot_top_districts()
    plot_kollam_case_study()

    print("✅ Visualizations saved to outputs/figures/")


if __name__ == "__main__":
    main()
