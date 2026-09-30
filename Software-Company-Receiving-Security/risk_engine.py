"""
Risk Engine Module: Translates technical alerts into quantified business risk.
Provides risk aggregation, baseline comparisons, and rollback simulation.
"""

import pandas as pd
import numpy as np

def calculate_aggregate_risk_metrics(alerts_df):
    """
    Computes overall organizational business risk score normalized (0 - 100),
    inherent vs residual risk, and risk reduction percentage.
    """
    if alerts_df.empty:
        return {
            "baseline_raw_risk": 0.0,
            "current_effective_risk": 0.0,
            "net_risk_reduction": 0.0,
            "reduction_percentage": 0.0,
            "risk_index_score": 0.0
        }
    
    total_raw_risk = alerts_df["raw_risk"].sum()
    total_effective_risk = alerts_df["effective_business_risk"].sum()
    net_reduction = total_raw_risk - total_effective_risk
    reduction_pct = (net_reduction / total_raw_risk * 100) if total_raw_risk > 0 else 0.0
    
    # Normalizing Business Risk Index (0 - 100)
    # Target maximum baseline risk threshold based on sample size
    max_possible_risk = len(alerts_df) * (10.0 * 5.0)  # max CVSS (10) * max Criticality (5)
    normalized_risk_index = round((total_effective_risk / max_possible_risk) * 100, 1)

    return {
        "baseline_raw_risk": round(total_raw_risk, 1),
        "current_effective_risk": round(total_effective_risk, 1),
        "net_risk_reduction": round(net_reduction, 1),
        "reduction_percentage": round(reduction_pct, 1),
        "risk_index_score": normalized_risk_index
    }

def get_risk_by_asset_tier(alerts_df):
    """Aggregates business risk distribution across Asset Tiers."""
    tier_summary = alerts_df.groupby("asset_tier").agg(
        total_alerts=("alert_id", "count"),
        open_alerts=("remediation_status", lambda s: (s == "Open").sum()),
        raw_risk=("raw_risk", "sum"),
        effective_risk=("effective_business_risk", "sum"),
        risk_reduced=("risk_reduction_achieved", "sum")
    ).reset_index()
    
    tier_summary["reduction_pct"] = np.where(
        tier_summary["raw_risk"] > 0,
        (tier_summary["risk_reduced"] / tier_summary["raw_risk"] * 100).round(1),
        0.0
    )
    return tier_summary

def get_control_effectiveness_table(alerts_df):
    """Measures quantifiable risk reduction attributable to each specific security control."""
    ctrl_summary = alerts_df.groupby(["control_id", "control_name", "control_status"]).agg(
        alerts_impacted=("alert_id", "count"),
        resolved_count=("remediation_status", lambda s: (s == "Resolved").sum()),
        total_risk_curbed=("risk_reduction_achieved", "sum")
    ).reset_index()
    
    ctrl_summary["resolution_rate"] = (
        (ctrl_summary["resolved_count"] / ctrl_summary["alerts_impacted"]) * 100
    ).round(1)
    
    ctrl_summary["total_risk_curbed"] = ctrl_summary["total_risk_curbed"].round(1)
    return ctrl_summary.sort_values(by="total_risk_curbed", ascending=False)
