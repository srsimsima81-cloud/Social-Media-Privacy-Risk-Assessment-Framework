# System Architecture

```text
User
  |
  v
Privacy Questionnaire
  |
  v
Input Validation
  |
  v
Privacy Feature Extraction
  |
  +--> Profile Analyzer
  +--> Personal Information Analyzer
  +--> Location Analyzer
  +--> Content Analyzer
  +--> Connection Analyzer
  +--> Tagging Analyzer
  +--> Account Security Analyzer
  +--> Third-Party App Analyzer
  +--> Social Engineering Analyzer
  +--> Digital Footprint Analyzer
  |
  v
Category Scores
  |
  v
Weighted Risk Scoring
  |
  v
Risk Classification
  |
  v
Findings Engine
  |
  v
Recommendation Engine
  |
  +--> Dashboard
  |
  +--> HTML Report
  |
  +--> Educational Improvement Simulation

Optional aggregate analytics:
derived scores only -> SQLite
```

## Component responsibilities

- `questionnaire.py`: defines safe questionnaire metadata.
- `scoring_engine.py`: converts responses to risk contributions and category/overall scores.
- `findings_engine.py`: maps risky indicators to explainable findings.
- `recommendation_engine.py`: maps findings to prioritized defensive guidance.
- `improvement_simulator.py`: re-runs the same scoring model after hypothetical changes.
- `database.py`: stores only derived assessment data.
- `report_generator.py`: creates an HTML report without raw answers.
- `app.py`: REST API and page routing.
