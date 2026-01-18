# UIDAI Hackathon 2026  
## Detecting Post-Stabilization Anomalies in Aadhaar Update Activity

---

## 1. Background & Motivation

The Aadhaar ecosystem continuously processes:
- **New enrolments**
- **Demographic updates** (name, address, DOB, etc.)
- **Biometric updates** (fingerprints, iris, etc.)

At a national scale, **updates are expected** — people move, age, correct details.  
However, **unusual patterns of updates** at the **district level** may indicate:

- operational bottlenecks  
- abnormal update behavior  
- data pipeline inconsistencies  
- regions that require administrative review  

The challenge is **not** to flag every spike, but to identify **meaningful, localized anomalies** while ignoring **system-wide noise**.

---

## 2. Problem Statement (Reframed Clearly)

> How can we reliably detect **district-level abnormal Aadhaar update behavior** while separating it from:
> - national system rollouts
> - seasonal effects
> - population size differences?

The solution must be:
- scalable  
- interpretable  
- reproducible  
- suitable for audit and governance  

---

## 3. Data Used

We analyzed three UIDAI API datasets:

| Dataset | What it Represents |
|------|------------------|
| Aadhaar Enrolment | New Aadhaar creations |
| Demographic Updates | Changes in demographic attributes |
| Biometric Updates | Changes in biometric attributes |

**Time Range:** January 2025 – December 2025  
**Granularity:** District-level, aggregated monthly  

> Raw data is excluded from the repository due to size and sensitivity.

---

## 4. Step-by-Step Methodology

### Step 1: Data Audit & Integrity Checks  
**Script:** `run_audit.py`

Before any modeling, we validated the data:
- checked date ranges
- counted null dates
- verified negative values
- measured monthly coverage

#### Key Finding
- **Jan–Feb 2025 shows extreme volatility nationwide**
- This volatility appears **uniform across India**, indicating **system initialization / rollout effects**, not district-specific issues

📌 **Important Insight:**  
Early spikes should **not** be treated as anomalies.

---

### Step 2: Temporal Aggregation  
**Script:** `run_temporal_aggregation.py`

- Daily records were aggregated into **district × month**
- This aligns analysis with policy and reporting cycles
- Reduces noise from daily operational fluctuations

---

### Step 3: Feature Engineering (Core Intelligence Layer)  
**Script:** `run_feature_engineering.py`

Raw counts alone are misleading.  
Large districts naturally have more updates.

We engineered **normalized behavioral metrics**, including:

#### Key Metrics Explained

| Metric | Meaning |
|-----|-------|
| Demographic Update Rate | How frequently demographic changes occur relative to baseline |
| Biometric Update Rate | Frequency of biometric changes |
| Update Imbalance Score | Mismatch between demographic and biometric activity |
| Month-over-Month Change | Sudden jumps in update behavior |
| District Z-Score | How abnormal a district is relative to itself |

📌 These metrics allow **fair comparison across districts of different sizes**.

---

### Step 4: Dual Anomaly Detection  
**Core Logic:** `anomaly_detection.py`

We deliberately used **two independent approaches**:

#### A. Statistical Detection
- Z-score thresholds
- imbalance conditions
- fully interpretable

#### B. Machine Learning Detection
- Isolation Forest
- unsupervised, multivariate
- detects rare combinations of behaviors

📌 **Why both?**  
- Statistical → explainable  
- ML → robust to complex patterns  

Only overlapping signals are considered **high confidence**.

---

### Step 5: Anomaly Diagnostics  
**Script:** `run_anomaly_diagnostics.py`

We analyzed:
- how many anomalies are detected by each method
- how many overlap

#### Result Summary
- Statistical only → many (sensitive)
- ML only → fewer (conservative)
- **Overlap → highest confidence**

This overlap forms the **actionable anomaly set**.

---

### Step 6: Post-Stabilization Filtering (Critical Step)  
**Script:** `run_post_stabilization_filter.py`

To avoid false alarms:
- **Jan–Feb 2025 removed** (system stabilization period)
- **Mar–Dec 2025 retained** as steady-state data

📌 This ensures we flag **operational anomalies**, not rollout artifacts.

---

### Step 7: District Risk Ranking  
**Script:** `run_district_ranking.py`

Districts were ranked based on:
- number of anomalous months
- persistence over time

📌 Repeated anomalies matter more than one-time spikes.

---

## 5. Case Study: Kollam, Kerala (April 2025)

- Detected **after system stabilization**
- Flagged by **both statistical and ML methods**
- Significant deviation from its own historical behavior

📌 This makes Kollam a **high-confidence, audit-worthy case**, not a random fluctuation.

---

## 6. Visual Analysis  
**Script:** `run_visualizations.py`

Generated judge-ready visualizations:
- Monthly anomaly trend (clear separation of rollout vs steady state)
- Top anomalous districts
- Detailed Kollam case study

Saved under `outputs/figures/`.

---

## 7. Final Outputs

| Output | Purpose |
|-----|-------|
| statistical_anomalies.csv | Explainable anomalies |
| ml_anomalies.csv | ML-detected anomalies |
| post_stabilization_anomalies.csv | Actionable anomalies |
| district_anomaly_ranking.csv | Audit priority |
| high_confidence_anomalies.csv | Strongest signals |

---

## 8. Final Conclusion

This project delivers a **policy-ready anomaly detection framework** that:

- separates system-wide noise from real district-level issues  
- balances interpretability and ML robustness  
- prioritizes sustained abnormal behavior  
- produces reproducible, audit-friendly outputs  

It is not a black-box model — it is a **decision-support system** suitable for governance, monitoring, and targeted investigation.

---

## 9. How to Reproduce the Entire Pipeline

```bash
python scripts/run_audit.py
python scripts/run_temporal_aggregation.py
python scripts/run_feature_engineering.py
python scripts/run_anomaly_detection.py
python scripts/run_anomaly_diagnostics.py
python scripts/run_post_stabilization_filter.py
python scripts/run_district_ranking.py
python scripts/run_visualizations.py

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
