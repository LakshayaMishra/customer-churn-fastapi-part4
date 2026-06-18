import os
import pytest
from fastapi.testclient import TestClient

# Core Microservice module target ingestion hook 
# Web configuration validation handler
try:
    from app.main import app
except ImportError:
    import sys
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    from app.main import app

client = TestClient(app)

# 🚀 TEST CASE 1: Validation Hook Endpoint Testing (/health)
def test_diagnostic_health_endpoint():
    print("\nExecuting Test Case 1: Checking Endpoint accessibility framework connectivity parameters...")
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() in [{"status": "ok"}, {"status": "degraded", "message": "API context engine running, but serialized model architecture lookup failure verified."}]

# 🚀 TEST CASE 2: Single Payload Core Boundary Contract Schema Checks (/predict)
def test_single_inference_scoring_flow():
    print("\nExecuting Test Case 2: Verification of input parameters structures...")
    mock_payload = {
        "customer_id": 9081,
        "order_frequency": 5,
        "total_spend": 1250.00,
        "recency_days": 12,
        "ticket_count": 0,
        "campaign_clicks": 3,
        "total_web_sessions": 15
    }
    response = client.post("/predict", json=mock_payload)
    assert response.status_code == 200
    
    data = response.json()
    # Explicit Pydantic data boundary validation checks
    assert "customer_id" in data
    assert "churn_probability" in data
    assert "predicted_class" in data
    assert "risk_level" in data
    assert "risk_explanation" in data
    assert data["customer_id"] == 9081
    assert 0.0 <= data["churn_probability"] <= 1.0
    assert data["predicted_class"] in [0, 1]
    assert data["risk_level"] in ["low", "medium", "high"]

# 🚀 TEST CASE 3: Bad Payload Validation Integrity Framework Checks (HTTP 422 Errors)
def test_invalid_payload_structural_rejection():
    print("\nExecuting Test Case 3: Running error-handling structure verification patterns...")
    # Passing negative values to parameters that strictly restrict bound intervals to check Pydantic behavior
    malformed_payload = {
        "customer_id": 9082
