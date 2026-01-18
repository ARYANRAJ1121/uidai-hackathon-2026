from src.audit import load_all, parse_dates
from src.temporal_aggregation import (
    aggregate_enrolment,
    aggregate_demographic,
    aggregate_biometric,
)
import os


def main():
    enrol, demo, bio = load_all()

    enrol = parse_dates(enrol)
    demo = parse_dates(demo)
    bio = parse_dates(bio)

    enrol_m = aggregate_enrolment(enrol)
    demo_m = aggregate_demographic(demo)
    bio_m = aggregate_biometric(bio)

    os.makedirs("data/processed", exist_ok=True)

    enrol_m.to_csv("data/processed/enrolment_monthly.csv", index=False)
    demo_m.to_csv("data/processed/demographic_monthly.csv", index=False)
    bio_m.to_csv("data/processed/biometric_monthly.csv", index=False)

    print("=== TEMPORAL AGGREGATION COMPLETE ===")
    print("Saved monthly datasets to data/processed/")


if __name__ == "__main__":
    main()
