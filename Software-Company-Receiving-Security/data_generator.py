"""
Data Generation Script for Security Control-Effectiveness Dashboard.
Simulates disconnected security tools, asset criticality, control telemetry,
vulnerabilities, incidents, and data freshness states.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# Seed for reproducibility
np.random.seed(42)
random.seed(42)

DISCONNECTED_TOOLS = [
    {"name": "CrowdStrike Falcon (EDR)", "category": "Endpoint", "telemetry_freq_mins": 5},
    {"name": "AWS GuardDuty", "category": "Cloud Infrastructure", "telemetry_freq_mins": 10},
    {"name": "Snyk Security", "category": "AppSec / SAST", "telemetry_freq_mins": 60},
    {"name": "Palo Alto Firewall", "category": "Network", "telemetry_freq_mins": 15},
    {"name": "Qualys VMDR", "category": "Vulnerability Management", "telemetry_freq_mins": 120},
    {"name": "SonarQube Code Quality", "category": "DevSecOps", "telemetry_freq_mins": 180},
]

ASSETS = [
    {"asset_id": "AST-101", "name": "Payment Gateway DB", "tier": "Tier 1 (Critical)", "criticality_score": 5.0, "owner": "FinTech Core"},
    {"asset_id": "AST-102", "name": "Customer Auth API", "tier": "Tier 1 (Critical)", "criticality_score": 5.0, "owner": "Identity Team"},
    {"asset_id": "AST-103", "name": "Order Management Service", "tier": "Tier 2 (High)", "criticality_score": 3.8, "owner": "E-Commerce Ops"},
    {"asset_id": "AST-104", "name": "Internal HR & Payroll Portal", "tier": "Tier 2 (High)", "criticality_score": 3.2, "owner": "Corporate IT"},
    {"asset_id": "AST-105", "name": "Customer Support Ticketing", "tier": "Tier 3 (Medium)", "criticality_score": 2.2, "owner": "Support Ops"},
    {"asset_id": "AST-106", "name": "Staging / QA Kubernetes Cluster", "tier": "Tier 3 (Low)", "criticality_score": 1.5, "owner": "DevOps Lab"},
    {"asset_id": "AST-107", "name": "Analytics Data Lake", "tier": "Tier 2 (High)", "criticality_score": 3.5, "owner": "BI Data Team"},
]

SECURITY_CONTROLS = [
    {"control_id": "CTL-01", "name": "Mandatory Hardware MFA", "intended_reduction": 0.45, "status": "Active"},
    {"control_id": "CTL-02", "name": "EDR Real-Time Quarantine", "intended_reduction": 0.35, "status": "Active"},
    {"control_id": "CTL-03", "name": "Automated OS Patching Cycle (7-Day SLA)", "intended_reduction": 0.30, "status": "Active"},
    {"control_id": "CTL-04", "name": "Cloud WAF Anti-DDoS & Bot Mitigation", "intended_reduction": 0.25, "status": "Active"},
    {"control_id": "CTL-05", "name": "CI/CD Pipeline Secrets Scanning", "intended_reduction": 0.20, "status": "Degraded"},
    {"control_id": "CTL-06", "name": "Zero-Trust Microsegmentation", "intended_reduction": 0.40, "status": "Inactive"},
]

def generate_telemetry_health():
    """Generates freshness status for disconnected tool feeds (Active, Stale, Missing)."""
    now = datetime.now()
    tool_health = []
    
    for tool in DISCONNECTED_TOOLS:
        roll = random.random()
        if roll < 0.70:
            status = "Active"
            last_heartbeat = now - timedelta(minutes=random.randint(1, tool["telemetry_freq_mins"]))
        elif roll < 0.90:
            status = "Stale (>24h)"
            last_heartbeat = now - timedelta(hours=random.randint(25, 72))
        else:
            status = "Missing (Offline)"
            last_heartbeat = now - timedelta(days=random.randint(4, 10))
            
        tool_health.append({
            "tool_name": tool["name"],
            "category": tool["category"],
            "expected_freq_mins": tool["telemetry_freq_mins"],
            "last_heartbeat": last_heartbeat.strftime("%Y-%m-%d %H:%M:%S"),
            "status": status,
            "latency_seconds": random.randint(120, 850) if status == "Active" else 99999
        })
    return pd.DataFrame(tool_health)

def generate_raw_alerts(num_alerts=250):
    """Generates synthetic security alerts from disparate tools."""
    now = datetime.now()
    alerts = []
    
    severities = ["Critical", "High", "Medium", "Low"]
    severity_weights = [0.10, 0.25, 0.40, 0.25]
    
    for i in range(1, num_alerts + 1):
        tool = random.choice(DISCONNECTED_TOOLS)
        asset = random.choice(ASSETS)
        severity = np.random.choice(severities, p=severity_weights)
        
        # Base technical vulnerability score (CVSS 0.0 - 10.0)
        cvss_map = {"Critical": round(random.uniform(9.0, 10.0), 1),
                    "High": round(random.uniform(7.0, 8.9), 1),
                    "Medium": round(random.uniform(4.0, 6.9), 1),
                    "Low": round(random.uniform(1.0, 3.9), 1)}
        cvss = cvss_map[severity]
        
        # Remediation & control state
        is_remediated = random.random() < 0.65
        associated_control = random.choice(SECURITY_CONTROLS)
        
        # Days open
        days_open = random.randint(0, 45) if not is_remediated else random.randint(0, 15)
        
        # Inherent Raw Technical Risk = CVSS * Asset Criticality
        raw_tech_risk = round(cvss * asset["criticality_score"], 2)
        
        # Effective Business Risk:
        # Defense-in-depth security controls (preventative + compensating) mitigate exposure
        if associated_control["status"] == "Active":
            if is_remediated:
                # Fully patched + active control
                reduction_factor = random.uniform(0.82, 0.94)
            else:
                # Compensating control in place (e.g., WAF virtual patch / EDR block)
                reduction_factor = random.uniform(0.50, 0.68)
            effective_risk = round(raw_tech_risk * (1 - reduction_factor), 2)
        elif associated_control["status"] == "Degraded":
            reduction_factor = random.uniform(0.20, 0.35) if is_remediated else random.uniform(0.10, 0.20)
            effective_risk = round(raw_tech_risk * (1 - reduction_factor), 2)
        else:
            reduction_factor = 0.0
            effective_risk = raw_tech_risk

        risk_reduction_points = round(raw_tech_risk - effective_risk, 2)
        
        alert_timestamp = now - timedelta(days=days_open, hours=random.randint(1, 23))

        alerts.append({
            "alert_id": f"ALT-{1000 + i}",
            "timestamp": alert_timestamp.strftime("%Y-%m-%d %H:%M"),
            "source_tool": tool["name"],
            "tool_category": tool["category"],
            "asset_id": asset["asset_id"],
            "asset_name": asset["name"],
            "asset_tier": asset["tier"],
            "criticality_score": asset["criticality_score"],
            "severity": severity,
            "cvss_score": cvss,
            "control_id": associated_control["control_id"],
            "control_name": associated_control["name"],
            "control_status": associated_control["status"],
            "remediation_status": "Resolved" if is_remediated else "Open",
            "raw_risk": raw_tech_risk,
            "effective_business_risk": effective_risk,
            "risk_reduction_achieved": risk_reduction_points
        })
        
    return pd.DataFrame(alerts)

if __name__ == "__main__":
    print("Generating synthetic security telemetry...")
    health_df = generate_telemetry_health()
    alerts_df = generate_raw_alerts(300)
    
    health_df.to_csv("tool_telemetry_health.csv", index=False)
    alerts_df.to_csv("security_alerts_telemetry.csv", index=False)
    print("Saved 'tool_telemetry_health.csv' and 'security_alerts_telemetry.csv' successfully.")
