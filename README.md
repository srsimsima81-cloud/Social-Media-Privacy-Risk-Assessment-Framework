# Social Media Privacy Risk Assessment Framework

> A privacy-preserving cybersecurity framework for assessing social-media privacy exposure, identifying risky configuration and behavior patterns, and generating actionable recommendations.

## Overview

The **Social Media Privacy Risk Assessment Framework** is a defensive cybersecurity and privacy-awareness application designed to help users understand how their social-media privacy settings and online behaviors may contribute to privacy exposure.

The application uses a **50-question privacy assessment questionnaire** covering profile visibility, personal information exposure, location privacy, content exposure, connections, tagging, account security, third-party applications, social engineering awareness, and digital footprint.

The system converts user-selected privacy indicators into category-level risk scores, calculates an overall privacy risk score, classifies the result into a risk level, generates findings and recommendations, and presents the results through a web dashboard and assessment report.

### Privacy-first design

This project intentionally **does not scrape social-media platforms or collect personal information about real individuals**.

It does not:

* Scrape real social-media profiles
* Enumerate or discover user accounts
* Bypass privacy controls
* Access private accounts
* Track individuals
* Collect passwords or authentication credentials
* Collect private messages
* Collect phone numbers, email addresses, or home addresses
* Collect exact real-world locations
* Perform surveillance or behavioral tracking

Instead, the application evaluates **self-reported privacy settings and behaviors** using predefined indicators.

---

# Key Features

## 1. 50-Question Privacy Assessment

The questionnaire contains 50 questions across 10 privacy and security categories.

### Profile Visibility

* Public profile visibility
* Search-engine discoverability
* Follower visibility
* Connection visibility

### Personal Information

* Phone-number visibility
* Email visibility
* Birthday visibility
* Home-related information
* Workplace
* Education
* Family and relationship information

### Location Privacy

* General location sharing
* Real-time check-ins
* Geotagging
* Travel plans
* Location patterns
* Workplace or study-location exposure

### Posts & Content

* Public posts
* Public photos
* Documents and screens appearing in photos
* Historical posts
* Audience review practices

### Friends & Followers

* Unknown connection requests
* Connection review
* Visibility of connections

### Tagging & Mentions

* Tag review
* Unrestricted tagging
* Unknown mentions
* Automatic tagged-post appearance

### Account Security

* MFA
* Unique passwords
* Password management
* Login alerts
* Recovery methods
* Active sessions
* Password reuse

### Third-Party Applications

* Connected-app reviews
* Unused integrations
* Excessive permissions
* Old social-login connections

### Social Engineering

* Suspicious-link awareness
* Verification-code protection
* Unexpected DMs
* Impersonation verification
* Suspicious giveaways

### Digital Footprint

* Old accounts
* Public comments
* Privacy-setting reviews
* Historical-post reviews
* Image metadata awareness

---

# Risk Assessment Workflow

```text
User
  │
  ▼
Privacy Questionnaire
  │
  ▼
Input Validation
  │
  ▼
Privacy Feature Extraction
  │
  ▼
Category Risk Analysis
  │
  ▼
Risk Scoring Engine
  │
  ▼
Overall Privacy Risk Score
  │
  ▼
Risk Classification
  │
  ├── Findings
  │
  ├── Recommendations
  │
  └── Improvement Simulation
          │
          ▼
    Privacy Dashboard
          │
          ▼
    Assessment Report
```

---

# Risk Scoring Model

The framework calculates risk across ten categories.

| Category             |   Weight |
| -------------------- | -------: |
| Profile Visibility   |      10% |
| Personal Information |      15% |
| Location Privacy     |      15% |
| Posts & Content      |      10% |
| Connections          |      10% |
| Tagging              |       5% |
| Account Security     |      15% |
| Third-Party Apps     |       5% |
| Social Engineering   |      10% |
| Digital Footprint    |       5% |
| **Total**            | **100%** |

Each category receives a score from:

```text
0 ─────────────────────────────── 100
Low exposure                 Higher exposure
```

The weighted category scores are combined to produce the overall assessment score.

## Risk Classification

|  Score | Classification |
| -----: | -------------- |
|   0–20 | LOW            |
|  21–40 | MODERATE       |
|  41–70 | HIGH           |
| 71–100 | CRITICAL       |

These thresholds and weights are **educational assumptions** intended for demonstration and awareness. They should not be treated as a validated professional risk standard.

A higher score represents **higher assessed privacy exposure within this framework**. It does not mean that an account has been compromised.

---

# Example Assessment

A fictional assessment might contain:

```text
Profile Visibility: PUBLIC
Phone Visibility: YES
Birthday Visibility: YES
Location Sharing: YES
Real-Time Check-ins: YES
Travel Plans: YES
Unknown Connections: OFTEN
Tag Review: NO
MFA: NO
Login Alerts: NO
Third-Party Apps Reviewed: NO
Historical Posts Reviewed: NO
```

The framework may produce:

```text
Overall Score: 72 / 100
Risk Level: CRITICAL
```

Example findings:

```text
HIGH PRIORITY

• Public contact information increases potential exposure.
• Real-time location sharing increases location exposure.
• MFA is not enabled.
• Login security alerts are disabled.
• Tag review is disabled.
• Connected applications have not been recently reviewed.
• Historical public content has not been reviewed.
```

Example recommendations:

```text
IMMEDIATE
• Enable MFA.
• Restrict unnecessary public contact information.
• Avoid public real-time location sharing.

IMPORTANT
• Enable tag review.
• Review connected applications and permissions.
• Review active sessions and devices.

GOOD PRACTICE
• Review historical public posts.
• Periodically review followers and connections.
• Review image metadata before public sharing.
```

---

# Improvement Simulator

The application includes a **what-if improvement simulator**.

Users can simulate privacy improvements such as:

* Hiding phone visibility
* Hiding birthday visibility
* Restricting location sharing
* Stopping public travel-plan sharing
* Rejecting unfamiliar connection requests
* Enabling tag review
* Enabling MFA
* Enabling login alerts
* Reviewing third-party applications
* Reviewing historical posts
* Reviewing privacy settings

Example:

```text
Current Assessment
────────────────────────
Score: 72 / 100
Level: CRITICAL

Simulated Improvements
────────────────────────
MFA: ENABLED
Tag Review: ENABLED
Location Sharing: RESTRICTED
Phone Visibility: RESTRICTED
Third-Party Apps: REVIEWED

Simulated Score
────────────────────────
34 / 100
MODERATE

Risk Reduction
────────────────────────
38 points
```

The simulator is an educational **what-if calculation** and is not a guarantee of future safety or risk reduction.

---

# Dashboard

The dashboard provides a visual overview of assessment results.

It can display:

* Overall assessment statistics
* Average risk score
* Risk-level distribution
* Category risk scores
* High-risk assessment count
* Category comparison charts
* Account-security indicators
* Privacy improvement information

Charts are implemented using **Chart.js**.

---

# Privacy Assessment Report

Each assessment can produce a report containing:

* Assessment ID
* Assessment date
* Overall score
* Risk classification
* Category scores
* Findings
* Recommendations
* Priority actions
* Privacy checklist
* Educational disclaimer

The report is designed to avoid including unnecessary sensitive information.

---

# Privacy-by-Design

The project follows privacy-by-design principles.

### Data Minimization

The system does not need actual personal information to perform the assessment.

### Purpose Limitation

Assessment data is used only for privacy-risk analysis and reporting.

### Least Privilege

The application does not require access to social-media accounts.

### Privacy by Default

The framework encourages restrictive privacy configurations and periodic reviews.

### User Control

Users provide the assessment information themselves and can use the improvement simulator to understand potential changes.

### Retention Limitation

The system is designed to retain derived assessment information rather than unnecessary personal information.

---

# Data Model

The application uses a relational database for assessment results.

## ASSESSMENTS

```text
assessment_id
overall_score
risk_level
created_at
```

## CATEGORY_SCORES

```text
category_score_id
assessment_id
category
score
```

## FINDINGS

```text
finding_id
assessment_id
category
finding_type
severity
description
```

## RECOMMENDATIONS

```text
recommendation_id
assessment_id
finding_type
recommendation
priority
```

The design intentionally avoids storing information such as:

```text
Phone numbers
Email addresses
Home addresses
Passwords
Exact locations
Private messages
Social-media credentials
```

---

# REST API

The backend exposes REST-style endpoints for the application.

| Method | Endpoint                               | Purpose                         |
| ------ | -------------------------------------- | ------------------------------- |
| POST   | `/api/assessment`                      | Create a privacy assessment     |
| GET    | `/api/assessment/{id}`                 | Retrieve an assessment          |
| GET    | `/api/assessment/{id}/recommendations` | Retrieve recommendations        |
| POST   | `/api/assessment/simulate-improvement` | Run improvement simulation      |
| GET    | `/api/dashboard/stats`                 | Retrieve dashboard statistics   |
| GET    | `/api/privacy-checklist`               | Retrieve questionnaire metadata |
| DELETE | `/api/assessment/{id}`                 | Delete an assessment            |

### Example assessment request

```json
{
  "answers": {
    "profile_visibility": "PUBLIC",
    "search_engine_visibility": "YES",
    "phone_public": "NO",
    "location_public": "NO",
    "mfa_enabled": "YES"
  }
}
```

The complete application sends all required questionnaire answers.

### Example response

```json
{
  "assessment_id": "A-123456",
  "overall_score": 42,
  "risk_level": "HIGH",
  "category_scores": {
    "Profile Visibility": 50,
    "Personal Information": 35,
    "Location Privacy": 40,
    "Account Security": 30
  }
}
```

---

# Project Structure

```text
Social-Media-Privacy-Risk-Assessment/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   │   ├── assessment_engine.py
│   │   ├── scoring_engine.py
│   │   ├── findings_engine.py
│   │   ├── recommendation_engine.py
│   │   └── improvement_simulator.py
│   └── utils/
│
├── frontend/
│   ├── index.html
│   ├── assessment.html
│   ├── dashboard.html
│   ├── simulator.html
│   ├── css/
│   └── js/
│       ├── assessment.js
│       ├── dashboard.js
│       └── simulator.js
│
├── data/
│   ├── generate_dataset.py
│   └── social_media_privacy_assessments.csv
│
├── reports/
├── screenshots/
├── tests/
├── docs/
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Synthetic Dataset

The project includes a synthetic dataset generator for testing and analysis.

The generator creates fictional assessment records containing privacy-risk indicators rather than real people's information.

Dataset location:

```text
data/social_media_privacy_assessments.csv
```

The project uses deterministic synthetic data generation so results can be reproduced during development and testing.

The dataset is intended for:

* Testing
* Demonstrations
* Data analysis
* Dashboard development
* Risk-model experimentation
* Academic presentation

It is **not collected from real social-media users**.

---

# Technology Stack

## Backend

* Python
* Flask
* SQLite
* REST API

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## Testing

* pytest

## Data

* CSV
* Synthetic dataset generation
* SQLite database

---

# Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd Social-Media-Privacy-Risk-Assessment
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Generate the synthetic dataset

```bash
python data/generate_dataset.py
```

## 5. Run tests

```bash
python -m pytest -q
```

## 6. Start the application

```bash
python -m backend.app
```

## 7. Open the application

```text
http://127.0.0.1:5000
```

Assessment:

```text
http://127.0.0.1:5000/assessment
```

Dashboard:

```text
http://127.0.0.1:5000/dashboard
```

Improvement simulator:

```text
http://127.0.0.1:5000/simulator
```

---

# Testing

The project includes automated tests covering important application behavior.

Testing areas include:

* Questionnaire validation
* Required fields
* Valid answer values
* Risk-score boundaries
* Risk classification
* Category scoring
* Weighted scoring
* Findings generation
* Recommendation generation
* Improvement simulation
* API responses
* Invalid input handling
* Privacy-safe data storage
* Report safety
* XSS-related input handling
* Assessment deletion

Run:

```bash
python -m pytest -q
```

---

# Threat Model

The framework considers privacy and security threats such as:

| Asset                | Threat                | Potential Exposure            | Control                 |
| -------------------- | --------------------- | ----------------------------- | ----------------------- |
| Account              | Account takeover      | Unauthorized access           | MFA                     |
| Identity information | Impersonation         | Public profile information    | Minimize exposure       |
| Contact information  | Phishing              | Public phone/email visibility | Restrict visibility     |
| Location privacy     | Location exposure     | Real-time location sharing    | Disable public location |
| Private content      | Unwanted disclosure   | Excessive public posting      | Audience controls       |
| Social relationships | Social engineering    | Public connection information | Review connections      |
| Third-party access   | Excessive permissions | Unused integrations           | Periodic app review     |

The framework focuses on **defensive awareness and risk reduction**, not attack execution.

---

# Privacy vs. Security

Privacy and security are related but different.

### Security

Security focuses on protecting accounts, systems, and information from unauthorized access.

Examples:

* MFA
* Strong unique passwords
* Login alerts
* Session management
* Recovery controls

### Privacy

Privacy focuses on controlling who can see, access, infer, or use information about an individual.

Examples:

* Profile visibility
* Contact-information visibility
* Location sharing
* Audience controls
* Tagging controls
* Historical content

An account can have strong security controls while still exposing excessive public information.

---

# Security Awareness

The project demonstrates common privacy and social-engineering awareness principles.

Users should be cautious with:

* Unexpected links
* Unknown connection requests
* Requests for verification codes
* Suspicious DMs
* Impersonation attempts
* Unusual prize or giveaway messages
* Requests for personal information

The framework does not generate phishing messages, attack scripts, or instructions for targeting real people.

---

# Image and Metadata Awareness

Public images can unintentionally reveal contextual information such as:

* Documents
* Screens
* Badges
* Workplace information
* School information
* Vehicles
* Travel context
* Location metadata

The project treats metadata awareness as a privacy education topic.

It does not perform individual tracking or infer someone's location from public images.

---

# Industry Relevance

This project demonstrates concepts relevant to:

* Cybersecurity
* Privacy Engineering
* Security Awareness
* Governance, Risk & Compliance
* Identity and Access Management
* Digital Risk Management
* Application Security
* Security Consulting
* Privacy Operations

Relevant roles include:

* Cybersecurity Analyst
* Privacy Analyst
* GRC Analyst
* SOC Analyst
* Security Consultant
* IAM Analyst
* Security Awareness Specialist
* Privacy Engineer

---

# Learning Outcomes

This project demonstrates practical experience with:

* Privacy-risk modeling
* Risk scoring
* Feature extraction
* Security questionnaires
* REST API development
* Flask application development
* Database design
* Input validation
* Automated testing
* Synthetic dataset generation
* Dashboard development
* Data visualization
* Privacy-by-design principles
* Threat modeling
* Security awareness
* Defensive cybersecurity engineering

---

# Limitations

This framework is an educational and demonstrative system.

It does **not**:

* Determine whether an actual account has been compromised
* Guarantee privacy or security
* Perform social-media monitoring
* Scan social-media platforms
* Identify real individuals
* Predict whether a person will be attacked
* Determine the actual probability of compromise
* Replace a professional privacy assessment
* Provide legal or regulatory compliance certification

Risk weights and thresholds are configurable educational assumptions and should be validated before being used for professional risk decisions.

---

# Future Enhancements

Potential future improvements include:

* Role-based access control
* Authentication for organizational deployments
* PostgreSQL support
* PDF report generation
* Configurable scoring profiles
* Organization-level dashboards
* Privacy-policy mapping
* GDPR/DPDP-oriented awareness mapping
* Assessment history
* Exportable JSON/CSV reports
* More granular privacy controls
* Accessibility improvements
* Expanded automated security testing
* Docker deployment
* CI/CD integration
* Security headers and production hardening

---

# Ethical and Responsible Use

This project is intended for:

* Education
* Cybersecurity awareness
* Privacy self-assessment
* Defensive security research
* Academic projects
* Security training
* Demonstration and portfolio purposes

Use only information that you are authorized to assess.

Do not use this framework to:

* Profile real individuals without authorization
* Collect private information
* Bypass privacy controls
* Track people
* Enumerate accounts
* Monitor individuals
* Perform unauthorized reconnaissance

---


## Project Summary

The **Social Media Privacy Risk Assessment Framework** demonstrates how privacy configuration and self-reported online behaviors can be transformed into a structured cybersecurity risk assessment.

The project combines:

```text
Privacy Questionnaire
        +
Feature Extraction
        +
Risk Scoring
        +
Threat Modeling
        +
Findings
        +
Recommendations
        +
Improvement Simulation
        +
Dashboard
        +
Reporting
```

into a single privacy-focused defensive cybersecurity application.

> **Disclaimer:** This project is an educational privacy-risk assessment framework. Its scores represent modeled exposure based on the questionnaire and configured assumptions. They are not guarantees of compromise, safety, or real-world risk.
