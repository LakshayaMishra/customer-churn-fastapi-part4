# Part 4: Production FastAPI Churn Scoring Microservice

A production-grade Python microservice framework implementing FastAPI, structural Pydantic data contract validation layers, and automated testing engines designed to expose our predictive churn engine to external corporate CRM networks.

## 📁 Repository Deliverables Architecture
* `app/main.py` - Primary FastAPI engine housing schema validations, `/health`, `/predict`, and `/batch_predict` route implementations.
* `train_model.py` - Standalone pipeline execution script to recreate and dump the serialized machine learning model asset.
* `test_api.py` - Structural verification suites covering input bounds, runtime states, and type safety constraints.
* `model.pkl` - Serialized production pipeline classifier binary.
* `monitoring_plan.md` - Production infrastructure governance guide tracking drift indicators, re-training cycles, and responsible use rules.
* `requirements.txt` - Module deployment manifest list.

---

## 🛠️ Local Environment Deployment Guide

### 1. Recreate the Virtual Workspace & Install Modules
```bash
pip install -r requirements.txt
