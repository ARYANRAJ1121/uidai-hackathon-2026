import pandas as pd
import os

from src.feature_engineering import (
    build_monthly_base,
    add_rates,
    add_mom_deltas,
    add_within_district_zscores,
)


def main():
    enrol = pd.read_csv("data/processed/enrolment_monthly.csv")
    demo = pd.read_csv("data/processed/demographic_monthly.csv")
    bio = pd.read_csv("data/processed/biometric_monthly.csv")

    df = build_monthly_base(enrol, demo, bio)
    df = add_rates(df)
    df = add_mom_deltas(df)
    df = add_within_district_zscores(df)

    df.to_csv("data/processed/monthly_features.csv", index=False)

    print("=== FEATURE ENGINEERING COMPLETE ===")
    print(f"Rows: {len(df)}")
    print("Saved: data/processed/monthly_features.csv")


if __name__ == "__main__":
    main()
