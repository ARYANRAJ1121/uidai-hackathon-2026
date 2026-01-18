from src.audit import load_all, parse_dates, date_audit, negative_check
import os
import json

def main():
    enrol, demo, bio = load_all()

    enrol = parse_dates(enrol)
    demo  = parse_dates(demo)
    bio   = parse_dates(bio)

    report = {
        "enrolment": date_audit(enrol),
        "demographic": date_audit(demo),
        "biometric": date_audit(bio),
        "negative_values": {
            "enrolment": negative_check(
                enrol, ["age_0_5", "age_5_17", "age_18_greater"]
            ),
            "demographic": negative_check(
                demo, ["demo_age_5_17", "demo_age_17_"]
            ),
            "biometric": negative_check(
                bio, ["bio_age_5_17", "bio_age_17_"]
            ),
        },
    }

    os.makedirs("outputs/audit", exist_ok=True)

    with open("outputs/audit/date_audit_summary.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    print("\n=== DATA AUDIT COMPLETED ===")
    for k, v in report.items():
        print(f"\n{k.upper()}")
        print(v)

if __name__ == "__main__":
    main()
