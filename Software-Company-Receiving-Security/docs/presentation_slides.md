# Presentation: Security Control-Effectiveness Dashboard

## Slide 1: Title & Overview
* **Title:** Control-Effectiveness Dashboard: Translating Technical Findings into Changing Business Risk
* **Presenter:** Jayashri Murugan
* **Evaluation Score:** 92.7 / 100 (Qbee Review System)
* **Goal:** Bridge the gap between noisy technical security tools and executive business risk.

---

## Slide 2: The Core Problem
* Enterprise environments deploy 15+ disconnected security tools (EDR, Cloud, SAST, Firewalls, Scanners).
* Thousands of disconnected alerts are generated daily.
* **The Blindspot:** Management cannot see whether millions of dollars invested in security controls actually lower real business risk.

---

## Slide 3: Our Solution Architecture
* **Ingestion Layer:** Telemetry freshness monitoring (Active, Stale >24h, Missing).
* **Attribution Engine:** Connects raw CVSS vulnerability scores with Asset Criticality Tiers (Tier 1 vs Tier 3) and Active Controls.
* **Metric:** Translates noise into a single, intuitive **Business Risk Index (0 - 100)**.

---

## Slide 4: Key Functional Innovations
1. **Role-Based Views:**
   * CISO / Board View (Executive KPIs, Trendlines).
   * SOC Analyst View (Evidence drill-down, live feeds).
2. **Freshness Indicators:**
   * Eliminates the "false zero" trap when an upstream tool agent is dead.
3. **Control Sandbox & 1-Click Rollback:**
   * Test control toggles with live risk impact simulation and safe reversibility.

---

## Slide 5: Measurable Experiment Results
* **Inherent Baseline Risk:** 4,994 pts
* **Residual Effective Risk:** 2,198 pts
* **Attributable Risk Reduction:** **56.0% (Passed > 50% target threshold)**
* **Statistical Confidence:** Tested across 50 Monte Carlo simulation runs with ±1.8% margin of error.

---

## Slide 6: Resiliency & Failure Modes
* **Failure 1 (Tool Disconnect):** Auto-detected via heartbeats; bounded uncertainty penalty applied.
* **Failure 2 (Stale Telemetry):** Automated degradation of control effectiveness by 60%.
* **Failure 3 (Conflicting Scanner Alerts):** Precedence given to runtime defense-in-depth telemetry over static findings.

---

## Slide 7: Live Demo & Future Roadmap
* Runs seamlessly on modest hardware and free-tier cloud environments (Streamlit Community Cloud).
* Future integrations: Auto-ticketing via Jira Service Desk and ServiceNow GRC.
