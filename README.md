# UIDAI Data Hackathon 2026  
## Temporal Analysis of Aadhaar Enrolment and Update Patterns

### Problem Context
The UIDAI Aadhaar ecosystem continuously records new enrolments as well as
demographic and biometric updates. Understanding how these activities evolve
over time is critical for ensuring system stability, data quality, and
effective policy decisions.

This project analyzes Aadhaar enrolment, demographic update, and biometric
update data to uncover:
- temporal trends,
- structural events,
- and anomalous behavior across states and districts.

### Objective
To identify meaningful patterns and anomalies over time in Aadhaar enrolments
and updates that can inform system monitoring and administrative
decision-making.

Rather than relying on static aggregates or arbitrary risk scores, we focus on:
- time-series behavior,
- month-over-month changes,
- and deviations from a region’s own historical baseline.

### High-Level Approach
1. Data Audit & Validation  
2. Temporal Aggregation  
3. Feature Engineering  
4. Anomaly Detection  
5. Interpretation & Visualization  

### Repository Structure
- data/ — Raw and processed datasets  
- notebooks/ — Step-by-step analytical workflow  
- src/ — Reusable preprocessing and modeling logic  
- outputs/ — Figures and tables for final submission  
