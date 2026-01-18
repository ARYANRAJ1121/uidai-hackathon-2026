# UIDAI Hackathon 2026  
## Post-Stabilization Anomaly Detection in Aadhaar Update Patterns

---

## Problem Statement

The UIDAI (Aadhaar) ecosystem processes large-scale **enrolments**, **demographic updates**, and **biometric updates** across India.  
While regular updates are expected, **unusual or inconsistent update patterns** at the district level may indicate:

- operational inefficiencies  
- system migration or rollout effects  
- data pipeline inconsistencies  
- regions requiring audit or policy attention  

The challenge is to **identify meaningful, localized anomalies** while avoiding false positives caused by **system-wide initialization noise**.

---

## Objective

Build a **reproducible, audit-ready anomaly detection pipeline** that:

1. Validates temporal integrity of UIDAI datasets  
2. Normalizes update behavior across districts of different sizes  
3. Detects anomalies using both statistical and ML methods  
4. Filters rollout-phase noise to isolate steady-state behavior  
5. Produces interpretable, actionable outputs for decision-making  

---

## Data Overview

Three UIDAI API datasets were analyzed:

| Dataset | Description |
|------|-----------|
| Aadhaar Enrolment | New enrolments by age group |
| Demographic Updates | Demographic changes |
| Biometric Updates | Biometric changes |

**Coverage:** January 2025 – December 2025  
**Granularity:** Aggregated to district-month level  

> Raw data is excluded from the repository due to size and sensitivity.

---

## Methodology

### 1. Data Audit & Temporal Validation  
**Script:** `scripts/run_audit.py`

- Verified date ranges, null dates, and negative values  
- Identified large global instability during **Jan–Feb 2025**

**Conclusion:** Early-period anomalies represent **system initialization**, not localized risk.

---

### 2. Temporal Aggregation  
**Script:** `scripts/run_temporal_aggregation.py`

- Aggregated daily records to **(state, district, year_month)**  
- Removed high-frequency noise and aligned with reporting cycles  

---

### 3. Feature Engineering  
**Script:** `scripts/run_feature_engineering.py`

Engineered normalized behavioral features:
- Demographic update rate  
- Biometric update rate  
- Update imbalance across modalities  
- Month-over-month change  
- Within-district Z-scores  

This ensures fair comparison across districts of different scales.

---

### 4. Dual Anomaly Detection  
**Core Logic:** `src/anomaly_detection.py`  
**Runner:** `scripts/run_anomaly_detection.py`

Two complementary methods were applied:

- **Statistical Detection:** Z-score and imbalance thresholds (highly interpretable)  
- **ML Detection:** Isolation Forest (unsupervised, multivariate rarity)  

Outputs from both were retained for comparison.

---

### 5. Anomaly Diagnostics  
**Script:** `scripts/run_anomaly_diagnostics.py`

- Analyzed overlap between statistical and ML anomalies  
- Identified **high-confidence anomalies** where both methods agreed  

---

### 6. Post-Stabilization Filtering  
**Script:** `scripts/run_post_stabilization_filter.py`

- Explicitly removed **Jan–Feb 2025** (system rollout phase)  
- Retained **Mar–Dec 2025** as steady-state operational data  

**Result:** 340 actionable post-stabilization anomalies.

---

### 7. District Risk Ranking  
**Script:** `scripts/run_district_ranking.py`

Districts were ranked by:
- number of anomalous months  
- persistence over time  

This prioritizes **sustained abnormal behavior**, not one-off spikes.

---

## Key Insight (Case Study)

**Kollam, Kerala — April 2025**

- Detected after system stabilization  
- Flagged by both statistical and ML methods  
- Deviated significantly from its own historical baseline  

This represents a **high-confidence, audit-worthy anomaly**.

---

## Visual Outputs  
**Script:** `scripts/run_visualizations.py`

Generated judge-ready artifacts:
- Monthly anomaly trend (rollout vs steady-state separation)  
- Top districts by persistent anomalies  
- Kollam district case study  

Saved under `outputs/figures/`.

---

## Final Outputs

| File | Description |
|----|-----------|
| `statistical_anomalies.csv` | Statistical anomalies |
| `ml_anomalies.csv` | ML anomalies |
| `post_stabilization_anomalies.csv` | Actionable anomalies |
| `district_anomaly_ranking.csv` | Audit priority list |
| `high_confidence_anomalies.csv` | Stat ∩ ML overlap |

---

## Conclusion

This project delivers a **practical anomaly detection framework** that:

- separates system-wide noise from localized risk  
- combines interpretability with ML robustness  
- prioritizes districts based on persistent behavior  
- produces reproducible, audit-ready outputs  

The result is a **decision-support pipeline**, not a black-box model, suitable for real-world governance and monitoring.

---

## How to Reproduce

```bash
python scripts/run_audit.py
python scripts/run_temporal_aggregation.py
python scripts/run_feature_engineering.py
python scripts/run_anomaly_detection.py
python scripts/run_anomaly_diagnostics.py
python scripts/run_post_stabilization_filter.py
python scripts/run_district_ranking.py
python scripts/run_visualizations.py

Repository Structure

uidai-hackathon-2026/
├── data/
│   ├── raw/            # ignored
│   └── processed/
├── src/
│   └── anomaly_detection.py
├── scripts/
│   └── run_*.py
├── outputs/
│   ├── anomalies/
│   └── figures/
├── README.md
└── requirements.txt

