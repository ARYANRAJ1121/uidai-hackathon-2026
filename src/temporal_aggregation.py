import pandas as pd


def add_year_month(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df[df["date"].notna()]
    df["year_month"] = df["date"].dt.to_period("M").astype(str)
    return df


def aggregate_enrolment(df: pd.DataFrame) -> pd.DataFrame:
    df = add_year_month(df)
    df["enrolment_total"] = (
        df["age_0_5"] + df["age_5_17"] + df["age_18_greater"]
    )
    return (
        df.groupby(["year_month", "state", "district"], as_index=False)
        ["enrolment_total"]
        .sum()
    )


def aggregate_demographic(df: pd.DataFrame) -> pd.DataFrame:
    df = add_year_month(df)
    df["demographic_total"] = (
        df["demo_age_5_17"] + df["demo_age_17_"]
    )
    return (
        df.groupby(["year_month", "state", "district"], as_index=False)
        ["demographic_total"]
        .sum()
    )


def aggregate_biometric(df: pd.DataFrame) -> pd.DataFrame:
    df = add_year_month(df)
    df["biometric_total"] = (
        df["bio_age_5_17"] + df["bio_age_17_"]
    )
    return (
        df.groupby(["year_month", "state", "district"], as_index=False)
        ["biometric_total"]
        .sum()
    )
