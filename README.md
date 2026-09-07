# Software-Company-Receiving-Security
# PROJECT PROGRESS REPORT: REVIEW 1 (35% COMPLETION)

## Project Title:
Control-Effectiveness Dashboard: Translating Security Alerts into Measurable Business Risk

---

## 1. Project Overview
The objective of this project is to develop a centralized Control-Effectiveness Dashboard that bridges the gap between raw technical security metrics and high-level business risk. Modern enterprise environments generate massive volumes of alerts across disconnected security tools. This project ingests these fragmented data streams, correlates technical findings with business assets, and quantifies whether existing security controls are effectively reducing organizational risk exposure.

---

## 2. Problem Statement
Enterprise security operations currently deploy isolated tools such as SIEM, Vulnerability Scanners, EDR, and Ticketing/ITSM systems. Because these tools operate in functional silos:
- Management and executive stakeholders lack visibility into aggregate business risk.
- High-volume alerts cause operational fatigue without asset-criticality-based prioritization.
- Organizations cannot quantitatively assess the return on investment (ROI) or efficacy of their implemented security controls.

Our proposed solution addresses this by aggregating multi-source security feeds into an automated risk scoring engine, presenting unified governance metrics on an interactive dashboard.

---

## 3. Architecture & Technical Stack

### A. Architectural Components Designed
1. Data Ingestion Layer: Connectors to parse alerts, vulnerability reports, and asset inventories.
2. Data Processing & Normalization Layer: Cleansing, schema unification, deduplication, and relational mapping.
3. Risk Calculation Engine: Deterministic, mathematical evaluation of multi-factor risk scores.
4. Dashboard & Visualization Module: Role-based executive summaries, trend lines, and drill-down tables.
5. Audit & Governance Logging Module: Tamper-evident logging of calculation parameters and system changes.

### B. Technology Stack
- Core Programming Language: Python 3.10+
- Data Analysis & Transformation: Pandas, NumPy
- Web Application Framework: Streamlit / Flask
- Database Management: SQLite / MySQL
- Data Visualization: Plotly / Power BI

---

## 4. Work Completed (35% Milestone Achieved)

### Phase 1 – Requirement Analysis & Scoping
- Evaluated key stakeholder requirements (SOC Leads, CISOs, Compliance Auditors).
- Formulated business risk metrics aligned with standard frameworks (NIST CSF and CIS Controls).
- Finalized functional and non-functional specifications.

### Phase 2 – Dataset Preparation & Engineering
Constructed comprehensive synthetic datasets to simulate enterprise security environments:
- Security Alerts: Synthetic SIEM & EDR telemetry containing event types, severities, and timestamps.
- Asset Inventory: IP mappings, hostname data, departmental ownership, and business criticality ratings (Tiers 1–5).
- Vulnerability Data: CVE records, CVSS v3.1 base metrics, and patch remediation states.
- Incident & Remediation Records: Ticket IDs, Mean Time to Detect/Remediate (MTTD/MTTR), and SLA status.

### Phase 3 – System & Database Design
- Designed normalized Relational Database Schema (ER modeling connecting Assets, Alerts, Vulnerabilities, and Controls).
- Created responsive UI wireframes for executive and analytical views.
- Mathematically verified the core risk scoring algorithm with edge-case tests.

---

## 5. Current Modules Developed & Repository Structure

### Developed Modules:
1. `alert_ingestion.py`: Implements parsing of multi-format logs (JSON/CSV) into standardized schemas.
2. `asset_criticality.py`: Evaluates asset tiers based on operational impact and data sensitivity.
3. `vulnerability_tracker.py`: Tracks unresolved CVEs and correlates them with existing host inventories.
4. `risk_engine.py`: Computes normalized business risk scores.

### Repository & Commit Structure:
- `data/`: Sample datasets (`assets.csv`, `alerts.csv`, `vulnerabilities.csv`, `incidents.csv`)
- `src/`: Core Python modules for ingestion, processing, and risk calculation
- `schema/`: Database ER diagram and SQL table definitions
- `tests/`: Unit test scripts validating scoring logic consistency
- Regular commits reflect iterative implementation across requirements, data engineering, and module modeling.

---

## 6. Risk Calculation Mathematical Formulation

The core business risk calculation logic is formulated as:

Business Risk Score = Asset Criticality × Vulnerability Severity × Incident Impact × Control Effectiveness

Where:
- Asset Criticality: Rating scaled from 1.0 (Low) to 5.0 (Mission-Critical).
- Vulnerability Severity: Normalized CVSS v3.1 score ranging from 0.1 to 10.0.
- Incident Impact: Multiplier based on active exploitability / breach status (1.0 to 2.0).
- Control Effectiveness: Inverse mitigation factor (0.1 to 1.0), where lower values represent stronger control defenses.
- Final Risk Score is normalized onto a standardized 0–100 index for executive readability.

---

## 7. Expected Dashboard Features
- Role-Based Access Control (RBAC): Dedicated views for Executive Leadership, Risk Officers, and SOC Engineers.
- Risk Trend Analytics: Historical tracking of organizational risk reduction over time.
- Asset Risk Ranking: Prioritized ranking of vulnerable assets requiring immediate patching.
- Control Effectiveness Breakdown: Visual metrics evaluating individual control performance (EDR, Firewall, MFA).
- Audit Trail Logs: Traceability of all ingested alerts, scoring adjustments, and user actions.

---

## 8. Challenges Identified & Mitigation Strategies
1. Disparate Data Formats: Inconsistent naming and severity scales across vendors.
   - Mitigation: Developed a unified schema dictionary and transformation pipeline in Pandas.
2. Score Skewness & Normalization: Multiplying four independent variables can cause wide variances.
   - Mitigation: Applied boundary normalization algorithms to maintain consistent 0–100 scoring.
3. Data Freshness: Stale logs could misrepresent current risk posture.
   - Mitigation: Implemented SLA timestamp flags to alert users of outdated feeds.

---

## 9. Next Phase Plan (Remaining 65% Roadmap)
- Phase 4 (Next Milestone - 70%):
  - Complete full frontend dashboard development using Streamlit/Flask.
  - Implement dynamic filtering and drill-down analytical charts.
  - Integrate database persistence layer.
- Phase 5 (Final Review - 100%):
  - Add role-based authentication and immutable audit logs.
  - Conduct end-to-end integration testing and benchmark performance.
  - Finalize user acceptance testing (UAT) and project documentation.

---

## 10. Conclusion
The foundation of the project has been successfully completed, including requirements analysis, dataset generation, relational schema design, and baseline risk scoring modules. The project is strictly on schedule with 35% of milestones fulfilled.

Project Status: 35% Completed (Review 1 Stage Satisfied)
