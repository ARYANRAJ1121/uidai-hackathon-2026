# UIDAI Hackathon 2026 — Submission Summary  
## Post-Stabilization Anomaly Detection in Aadhaar Update Activity

---

## Problem Overview

The Aadhaar system processes millions of **enrolments, demographic updates, and biometric updates** every year.  
While updates are expected, **unusual district-level patterns** may indicate:

- operational inefficiencies  
- abnormal update behavior  
- data inconsistencies  
- regions requiring administrative attention  

The key challenge is to **distinguish meaningful local anomalies from nationwide system effects** such as rollouts or seasonal trends.

---

## Objective

To design a **scalable, interpretable, and audit-ready framework** that identifies **district-level abnormal Aadhaar update behavior**, while filtering out system-wide noise.

---

## Data Used

- Aadhaar Enrolment data  
- Aadhaar Demographic update data  
- Aadhaar Biometric update data  

**Time Range:** Jan 2025 – Dec 2025  
**Granularity:** District × Month  

Raw data is excluded from the repository due to size and sensitivity.

---

## Key Methodology

### 1. Data Audit & Stabilization
- Verified date ranges, nulls, and invalid values
- Identified **Jan–Feb 2025** as a **system stabilization period** with nationwide volatility
- Excluded this period from anomaly decisioning

### 2. Temporal Aggregation
- Converted daily records into **monthly district-level summaries**
- Aligns analysis with governance and reporting cycles

### 3. Feature Engineering
Engineered normalized behavioral metrics to allow fair comparison across districts:
- Demographic update rate
- Biometric update rate
- Update imbalance score
- Month-over-month change
- District-wise Z-scores

### 4. Dual Anomaly Detection
Used **two independent approaches**:
- **Statistical detection** (thresholds, imbalance, Z-scores)
- **Machine Learning detection** (Isolation Forest)

Only overlapping signals are treated as **high-confidence anomalies**.

### 5. Post-Stabilization Filtering
- Retained anomalies only from **Mar–Dec 2025**
- Ensures focus on steady-state operational behavior

### 6. District Risk Ranking
- Ranked districts based on frequency and persistence of anomalies
- Prioritizes cases suitable for audit or review

---

## Key Results

- Clear separation between **system-wide rollout effects** and **localized anomalies**
- Significant reduction in false positives after stabilization filtering
- Identification of **high-confidence districts** flagged by both statistical and ML methods

### Case Highlight
- **Kollam, Kerala (April 2025)**  
  - Detected post-stabilization  
  - Flagged by both anomaly methods  
  - Represents a strong, explainable anomaly case

---

## Outputs Delivered

- Statistical anomalies
- ML-based anomalies
- High-confidence overlapping anomalies
- District-level risk rankings
- Judge-ready visualizations and case study plots

All outputs are reproducible via scripted execution.

---

## Conclusion

This solution provides a **policy-ready anomaly detection framework** that:
- avoids false alarms from system rollouts
- balances interpretability with ML robustness
- highlights persistent, district-level irregularities
- supports governance, monitoring, and targeted investigation

The framework is scalable, transparent, and suitable for real-world UIDAI oversight use.

---

## Reproducibility

Entire pipeline can be executed using Python scripts under `scripts/` in sequence.  
No notebooks are required.

---
