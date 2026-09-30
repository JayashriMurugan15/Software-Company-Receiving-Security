# Field-Workflow Map: Control-Effectiveness Architecture

This document maps how raw, disconnected security telemetry flows through ingestion, normalization, control-attribution, and business risk calculation to the executive dashboard.

## 🗺️ Architectural Workflow Diagram

```mermaid
flowchart TD
    subgraph Disconnected_Tools ["🔌 Disconnected Security Tools"]
        T1["CrowdStrike Falcon (EDR)"]
        T2["AWS GuardDuty (Cloud)"]
        T3["Snyk (AppSec/SAST)"]
        T4["Palo Alto Networks (Firewall)"]
        T5["Qualys VMDR (Vulnerability)"]
        T6["SonarQube (Code Quality)"]
    end

    subgraph Ingestion_Layer ["📡 Ingestion & Telemetry Monitor"]
        IN1["Heartbeat & Freshness Monitor"]
        IN2["Alert Aggregator & Deduplicator"]
        IN1 -->|Check Latency| F1{"Freshness Check"}
        F1 -->|Heartbeat < 1 hr| ST1["State: Active"]
        F1 -->|Heartbeat 1-24 hrs| ST2["State: Stale (Yellow)"]
        F1 -->|Heartbeat > 24 hrs| ST3["State: Missing (Red)"]
    end

    subgraph Risk_Engine ["⚙️ Risk Attribution Engine"]
        AC["Asset Criticality Mapper (Tier 1/2/3)"]
        CE["Control-Effectiveness Attribution"]
        CALC["Business Risk Formulation: Raw Risk vs Effective Risk"]
        AC --> CALC
        CE --> CALC
    end

    subgraph Presentation_Layer ["📊 Control-Effectiveness Dashboard"]
        V1["Executive Summary: CISO / Board View"]
        V2["Technical Drill-Down: SecOps View"]
        V3["Sandbox & Audit Rollback Engine"]
    end

    Disconnected_Tools --> Ingestion_Layer
    Ingestion_Layer --> Risk_Engine
    Risk_Engine --> Presentation_Layer
```

## 🔄 Data Field Transformation Matrix

| Raw Tool Field | Internal Schema Field | Purpose & Business Logic |
|---|---|---|
| `alert_source` / `scanner_id` | `source_tool` | Identifies tool provenance |
| `ip_address` / `hostname` | `asset_id` & `asset_tier` | Maps technical asset to business criticality (Tier 1: High value DB/Auth vs Tier 3: Staging) |
| `cvss_score` (0-10) | `cvss_score` | Quantifies technical vulnerability severity |
| `applied_policy` | `control_id` | Links alert to governing security control (e.g. MFA, EDR Quarantine, WAF) |
| `heartbeat_timestamp` | `status` (Active / Stale / Missing) | Determines confidence weight in the risk calculation |
