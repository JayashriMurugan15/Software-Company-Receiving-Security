# Failure-Mode Analysis: Edge Cases & Resiliency

This document analyzes at least three real-world edge and failure modes encountered when connecting disparate security telemetry tools, along with their mitigations implemented in this project.

---

### Failure Mode 1: Disconnected Tool Outage / API Blackout (e.g. CrowdStrike EDR Agent Offline)
* **Description:** An upstream security tool stops reporting telemetry due to network partition, expired API token, or agent crash.
* **Risk Without Solution:** Traditional SIEMs report "0 alerts", leading managers to mistakenly assume the company has zero security risk.
* **Implemented Mitigation:**
  * Active heartbeat tracker monitors incoming telemetry against expected frequency.
  * If no ping occurs within the threshold, state is explicitly marked as `Missing (Offline)`.
  * The risk calculation engine applies a bounded uncertainty penalty rather than showing false zero risk.

---

### Failure Mode 2: Stale Telemetry Delay (>24 Hours Lag)
* **Description:** A tool (such as Qualys VMDR or weekly vulnerability scans) provides data that is days old. Remediated vulnerabilities still appear open, or new zero-days are missed.
* **Risk Without Solution:** Executive decisions made on obsolete security posture.
* **Implemented Mitigation:**
  * Freshness indicators color-code data: `🟢 Active`, `🟡 Stale (>24h)`, `🔴 Missing`.
  * When stale data is detected, the dashboard shows an immediate global warning banner.
  * Controls linked to stale telemetry are automatically downgraded from `Active` to `Degraded` status (40% effectiveness haircut).

---

### Failure Mode 3: Conflicting Alerts & False Positives Across Tools
* **Description:** SAST (SonarQube/Snyk) flags a theoretical code vulnerability, while Network WAF and EDR show the vulnerability is unreachable and mitigated by active controls.
* **Risk Without Solution:** Alert fatigue for analysts and conflicting reports given to leadership.
* **Implemented Mitigation:**
  * Weighted risk attribution gives precedence to runtime telemetry (WAF, EDR) when calculating effective business risk.
  * Controls are explicitly tracked against asset criticality tiers, ensuring high-criticality assets (Tier 1) are never falsely marked low-risk without multi-source confirmation.
