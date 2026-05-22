# Automated HIPAA & HITRUST Risk Assessment Pipeline

## 📌 Project Overview
Early-stage healthcare startups face a dual challenge: they must rapidly build digital infrastructure while simultaneously complying with strict, complex healthcare regulations like the **HIPAA Security Rule** and the **HITRUST Common Security Framework (CSF)**. Traditional risk assessment workflows rely on static, manual spreadsheets that fail to scale alongside dynamic IT environments.

This project implements an automated, programmatic GRC (Governance, Risk, and Compliance) pipeline using Python and Pandas. The pipeline generates a simulated corporate asset infrastructure of 100 components, models context-specific threat scenarios, and dynamically maps those vulnerabilities directly to **HIPAA Safeguard Citations** and **HITRUST CSF 06.0 Controls**. Finally, it aggregates the data into an audit-ready executive cross-tabulation matrix and generates a presentation-ready data visualization dashboard.

---

## 🛠️ Technology Stack & Core Architecture
* **Language:** Python 3.11+
* **Data Science Libraries:** Pandas, NumPy
* **Visualization Engine:** Matplotlib, Seaborn
* **Shell Environment:** PowerShell / Windows Terminal

The pipeline is split into three decoupled operational stages:
1. **`simulate_assets.py` (Asset Baseline):** Programs the mock baseline inventory of 100 critical startup infrastructure items split among network gateways, backend identity access matrices, and operational production databases.
2. **`inject_vulnerabilities.py` (Threat Engine):** Implements a keyword-scanning algorithm that identifies infrastructure types and applies targeted risk severity ranks, mitigations, and compliance gap data.
3. **`analyze_compliance.py` (Framework Crosswalk & Visualization):** Computes explicit structural references down to regulatory sub-clauses, outputs terminal data summaries, and saves an executive stacked-bar dashboard.

---

## 📊 Executive Audit Findings

The automated pipeline evaluated 100 high-risk infrastructure components, grouping security flaws into their native compliance domains and risk tiers:

![Executive Compliance Dashboard](compliance_risk_dashboard.png)

### 🔍 Tactical GRC Insights
* **Concentrated Data Blast Radius:** While the **Technical/Physical Safeguards** category contains fewer individual assets (28), it contains the highest concentration of **Critical** vulnerabilities (12 out of 20). This represents production database servers and unmasked cloud buckets containing active ePHI—the highest immediate impact zone for an assessor.
* **Broad Identity Surface Area:** **Administrative Safeguards** represent the widest attack surface across the startup (38 total items). These risks represent identity sprawl, missing mobile device management (MDM) baseline profiles, and offboarding delays. These findings prioritize automated provisioning and stricter Role-Based Access Control (RBAC).

---

## 📂 Code Execution & Pipeline Re-generation

To clone this directory and run the data compilation pipeline from scratch, execute the following sequences within your local terminal:

### 1. Install Dependencies

```powershell
pip install pandas matplotlib seaborn

```

### 2. Execute Data Generation Pipeline

```powershell
# Step A: Spin up the 100 baseline business assets
py simulate_assets.py

# Step B: Scan assets and inject threat scenario vectors
py inject_vulnerabilities.py

# Step C: Apply regulatory mappings and export visual dashboard
py analyze_compliance.py

```

## 📈 Portfolio Deliverables & Artifacts

UPON PIPELINE EXECUTION RE-GEN, THE FOLLOWING VALIDATED METRIC LOGS AND DATA PACKETS WILL GENERATE DIRECTLY TO DISK STORAGE:

```text
[SYSTEM_OVERRIDE // ACTIVATING_ROBOTIC_GRC_PROTOCOL]
[CORE_PORTFOLIO_OUTPUT_STREAM // INITIALIZED]

* [DATA_LEDGER] -> final_portfolio_compliance_matrix_100.csv
    * [TYPE]: Audit-Ready Master Asset Registry
    * [METADATA]: Consolidates 100 enterprise business components, risk 
                  ratings, flaws, mitigations, and HIPAA/HITRUST crosswalks.
    * [STATUS]: Operational / Export Complete

* [GRAPHIC_MATRIX] -> compliance_risk_dashboard.png
    * [TYPE]: Executive Data Visualization Matrix
    * [METADATA]: Color-coded, stacked-bar rendering engineered via 
                  Matplotlib/Seaborn for presentation to stakeholders.
    * [STATUS]: Rasterized / Ready for Presentation

[SIGNAL_STABLE // END_ROBO_TRANSMISSION]

## 👤 Author & Contact
* **Developer:** George Jordan
* **Role:** GRC & HIPAA Compliance Specialist
* **Project Profile:** [LinkedIn](https://www.linkedin.com/in/georgejordan-grc) | [GitHub](https://github.com/GeoJordan)

---

## 📄 License
This project is open-source and available under the **MIT License**. Feel free to fork, modify, and utilize this pipeline for your own compliance mapping frameworks.
