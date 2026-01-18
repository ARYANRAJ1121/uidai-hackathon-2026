import pandas as pd


def build_monthly_base(enrol, demo, bio):
    df = enrol.merge(
        demo,
        on=["year_month", "state", "district"],
        how="left"
    ).merge(
        bio,
        on=["year_month", "state", "district"],
        how="left"
    )

    df = df.fillna(0)
    return df


def add_rates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["demo_update_rate"] = (
        df["demographic_total"] / (df["enrolment_total"] + 1)
    )

    df["bio_update_rate"] = (
        df["biometric_total"] / (df["enrolment_total"] + 1)
    )

    df["update_imbalance"] = (
        (df["demographic_total"] - df["biometric_total"])
        / (df["demographic_total"] + df["biometric_total"] + 1)
    )

    return df


def add_mom_deltas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["state", "district", "year_month"])

    df["demo_mom_delta"] = (
        df.groupby(["state", "district"])["demographic_total"].diff()
    )

    df["bio_mom_delta"] = (
        df.groupby(["state", "district"])["biometric_total"].diff()
    )

    return df


def add_within_district_zscores(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["demo_update_rate", "bio_update_rate"]:
        mean = df.groupby(["state", "district"])[col].transform("mean")
        std = df.groupby(["state", "district"])[col].transform("std")

        df[f"z_{col}"] = (df[col] - mean) / (std + 1e-9)

    return df
