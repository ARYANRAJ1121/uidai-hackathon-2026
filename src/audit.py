import pandas as pd
import glob
import os

RAW_DATA_PATH = "data/raw"

DATASETS = {
    "enrolment": "api_data_aadhar_enrolment",
    "demographic": "api_data_aadhar_demographic",
    "biometric": "api_data_aadhar_biometric",
}

def load_dataset(folder: str) -> pd.DataFrame:
    path = os.path.join(RAW_DATA_PATH, folder)
    files = glob.glob(os.path.join(path, "*.csv"))

    if not files:
        raise FileNotFoundError(f"No CSV files found in {path}")

    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

def load_all():
    enrol = load_dataset(DATASETS["enrolment"])
    demo  = load_dataset(DATASETS["demographic"])
    bio   = load_dataset(DATASETS["biometric"])
    return enrol, demo, bio

def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

def date_audit(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "null_dates": int(df["date"].isna().sum()),
        "min_date": df["date"].min(),
        "max_date": df["date"].max(),
        "unique_months": int(df["date"].dt.to_period("M").nunique()),
    }

def negative_check(df: pd.DataFrame, cols: list) -> bool:
    return (df[cols] < 0).any().any()
