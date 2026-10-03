# Defensive Threat Model

| Asset | Threat | Exposure | Impact | Existing Control | Recommended Control |
|---|---|---|---|---|---|
| Account | Account takeover | Weak authentication | High | Password | MFA, alerts, session review |
| Identity information | Impersonation | Public context | Medium/High | Privacy settings | Data minimization |
| Contact information | Phishing | Public phone/email | Medium | Awareness | Restrict visibility |
| Location | Unwanted physical exposure | Real-time sharing | High | Audience controls | Avoid real-time location |
| Private content | Unauthorized access | Weak access controls | High | Platform controls | MFA, session review |
| Social relationships | Social engineering | Public connections | Medium/High | User verification | Verify requests |
| App access | Data over-sharing | Unused permissions | Medium | Connected app settings | Least privilege |

Risk varies with platform, audience, threat actor, user context and available controls.
