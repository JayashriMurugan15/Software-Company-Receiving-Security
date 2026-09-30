# 🛡️ Control-Effectiveness Dashboard: Translating Technical Findings into Business Risk
[![Review Score](https://img.shields.io/badge/Qbee%20Review%20Score-92.7%20%2F%20100-brightgreen.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io)
---
## 📌 Problem Statement
A modern software company receives thousands of security alerts daily from disconnected tools (EDR, Cloud GuardDuty, SAST, Firewalls, Scanners). Management cannot see whether security controls are actually reducing real business risk, because raw technical alerts lack business context.
### 🎯 Objective
Develop an end-to-end Control-Effectiveness Dashboard that translates technical alert telemetry, asset criticality, vulnerabilities, and remediation statuses into a quantifiable Business Risk Index (0 - 100).
---
## 🚀 Key Features
- **👔 Executive / CISO Role View:** High-level Business Risk Index, risk trendlines, and risk distribution across asset tiers.
- **🛠️ Security Analyst Drill-Down:** Deep-dive into raw alerts, CVEs, CVSS scores, remediation states, and control attribution.
- **📡 Freshness Indicators:** Color-coded telemetry health (`🟢 Active`, `🟡 Stale >24h`, `🔴 Missing/Offline`).
- **⚙️ Control Sandbox & 1-Click Rollback:** Simulate the risk impact of activating/degrading controls with an audit trail and rollback safety net.
- **🧪 Measurable Experiment:** Demonstrates a 56.0% risk reduction attributable to active controls (Target > 50% PASSED ✅).
---
## 📦 Project Deliverables Checklist
- [x] **Field-Workflow Map:** `Software-Company-Receiving-Security/docs/field_workflow_map.md`
- [x] **Data-Generation Script:** `Software-Company-Receiving-Security/data_generator.py`
- [x] **Functional Dashboard Application:** `Software-Company-Receiving-Security/app.py`
- [x] **Experiment & Error Analysis:** `Software-Company-Receiving-Security/experiment_analysis.py` / `experiment.ipynb`
- [x] **3 Failure-Mode Analysis:** `Software-Company-Receiving-Security/docs/failure_mode_analysis.md`
- [x] **Stakeholder Feedback Summary:** `Software-Company-Receiving-Security/docs/user_feedback_summary.md`
- [x] **Presentation Slides:** `Software-Company-Receiving-Security/docs/presentation_slides.md`
---
## 💻 How to Run Locally
```bash
cd Software-Company-Receiving-Security
pip install -r requirements.txt
streamlit run app.py
Open your browser at http://localhost:8501 to view the interactive dashboard.

3. Paste pannitu, top-right corner-la irukura green color **`Commit changes...`** button-ah click pannidunga!
---
Idhai panna udaney ungal GitHub repository evaluators & professors paakkum podhu **top-tier corporate project maadhiri** romba neat-ah visual badges & description-oda kaattum! 🚀
10:13 AM
