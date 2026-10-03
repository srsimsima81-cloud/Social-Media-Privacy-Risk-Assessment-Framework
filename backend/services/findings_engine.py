FINDING_RULES = {
    "phone_public": ("Personal Information", "Public phone number", "HIGH",
                     "Your questionnaire indicates that a phone number is publicly visible."),
    "email_public": ("Personal Information", "Public personal email", "MODERATE",
                     "Your questionnaire indicates that a personal email address is publicly visible."),
    "birthday_public": ("Personal Information", "Public full birthday", "MODERATE",
                        "Your questionnaire indicates that your full birth date is publicly visible."),
    "home_info_public": ("Personal Information", "Home-related information exposed", "HIGH",
                         "Public content may reveal home-related context."),
    "workplace_public": ("Personal Information", "Workplace exposure", "MODERATE",
                         "Your workplace is reported as publicly visible."),
    "education_public": ("Personal Information", "Education exposure", "LOW",
                         "Your education history is reported as publicly visible."),
    "relationship_public": ("Personal Information", "Family/relationship exposure", "MODERATE",
                            "Family or relationship details are reported as publicly visible."),
    "location_public": ("Location Privacy", "Public location exposure", "HIGH",
                         "Your current/general location is reported as publicly shared."),
    "realtime_checkins": ("Location Privacy", "Real-time check-ins", "HIGH",
                          "Public real-time check-ins can increase immediate location exposure."),
    "geotagging": ("Location Privacy", "Geotagging", "MODERATE",
                   "Regular geotagging can expose contextual location information."),
    "travel_posts": ("Location Privacy", "Travel-plan exposure", "HIGH",
                     "Public travel plans can reveal absence or intended destinations."),
    "frequent_location_patterns": ("Location Privacy", "Repeated location patterns", "HIGH",
                                   "Repeated public posts may reveal routine locations."),
    "work_location_public": ("Location Privacy", "Work/study location exposure", "MODERATE",
                             "Public content may reveal a regular work or study location."),
    "posts_public": ("Posts & Content", "Public post exposure", "MODERATE",
                     "Many posts are reported as publicly visible."),
    "photos_public": ("Posts & Content", "Public photo exposure", "MODERATE",
                      "Personal photos are commonly visible to the public."),
    "documents_in_photos": ("Posts & Content", "Sensitive visual context", "HIGH",
                            "Photos may reveal documents, badges, screens, or other context."),
    "old_public_posts": ("Posts & Content", "Historical public posts", "MODERATE",
                         "Old public posts have not been regularly reviewed."),
    "unknown_connections": ("Friends / Followers", "Unknown connection requests", "HIGH",
                            "Unfamiliar connection requests are sometimes or often accepted."),
    "public_connections": ("Friends / Followers", "Public connections", "MODERATE",
                           "Unknown users can reportedly see your connections."),
    "anyone_can_tag": ("Tagging & Mentions", "Unrestricted tagging", "MODERATE",
                       "Anyone can reportedly tag the account without approval."),
    "unknown_mentions": ("Tagging & Mentions", "Unknown mentions", "MODERATE",
                         "Unknown users can reportedly mention the account."),
    "auto_tagged_posts": ("Tagging & Mentions", "Automatic tagged content", "MODERATE",
                          "Tagged posts can reportedly appear automatically."),
    "mfa_enabled": ("Account Security", "MFA disabled", "HIGH",
                    "Multi-factor authentication is not enabled."),
    "unique_password": ("Account Security", "Password uniqueness concern", "HIGH",
                        "The account may not use a unique password."),
    "password_manager": ("Account Security", "Password management gap", "MODERATE",
                         "A secure password-management method is not reported."),
    "login_alerts_enabled": ("Account Security", "Login alerts disabled", "MODERATE",
                             "Security/login alerts are not enabled."),
    "recovery_reviewed": ("Account Security", "Recovery settings not reviewed", "MODERATE",
                          "Recovery methods have not been recently reviewed."),
    "active_sessions_reviewed": ("Account Security", "Active sessions not reviewed", "MODERATE",
                                 "Active sessions/devices have not been recently reviewed."),
    "password_reuse_reported": ("Account Security", "Password reuse", "HIGH",
                                "The questionnaire indicates password reuse."),
    "third_party_apps_reviewed": ("Third-Party Apps", "Apps not reviewed", "MODERATE",
                                  "Connected third-party applications have not been recently reviewed."),
    "unused_apps_connected": ("Third-Party Apps", "Unused integrations", "MODERATE",
                              "Unused integrations are reportedly still connected."),
    "unnecessary_permissions": ("Third-Party Apps", "Unnecessary app permissions", "HIGH",
                                "Connected apps may retain permissions that are no longer needed."),
    "social_signin_connections": ("Third-Party Apps", "Old social sign-in connections", "MODERATE",
                                 "Old social sign-in connections have not been reviewed."),
    "suspicious_link_awareness": ("Social Engineering", "Unexpected-link awareness gap", "HIGH",
                                  "Unexpected links may not be independently verified."),
    "verification_code_sharing": ("Social Engineering", "Verification-code sharing", "CRITICAL",
                                  "Sharing security codes can enable account compromise."),
    "suspicious_dm_response": ("Social Engineering", "Suspicious DM response", "HIGH",
                               "Unexpected DMs requesting information or action may be answered."),
    "giveaway_awareness": ("Social Engineering", "Suspicious giveaway exposure", "MODERATE",
                           "Suspicious giveaway/prize links may be engaged with."),
    "old_accounts": ("Digital Footprint", "Old active accounts", "MODERATE",
                     "Old or unused accounts reportedly remain active."),
    "public_comments": ("Digital Footprint", "Public comment history", "MODERATE",
                        "A large public comment history can expand the digital footprint."),
    "privacy_settings_reviewed": ("Digital Footprint", "Privacy settings not reviewed", "HIGH",
                                  "Privacy settings have not been reviewed recently."),
    "historical_posts_reviewed": ("Digital Footprint", "Historical content not reviewed", "MODERATE",
                                  "Historical public content has not been recently reviewed."),
    "photo_metadata_awareness": ("Digital Footprint", "Photo metadata awareness gap", "MODERATE",
                                 "Photo metadata privacy implications are not regularly checked."),
}

def generate_privacy_findings(answers):
    findings = []
    for qid, rule in FINDING_RULES.items():
        answer = str(answers.get(qid, "")).upper()
        triggered = False
        if qid == "unknown_connections":
            triggered = answer in {"SOMETIMES", "OFTEN", "ALWAYS"}
        elif qid in {"mfa_enabled","unique_password","password_manager","login_alerts_enabled",
                     "recovery_reviewed","active_sessions_reviewed","third_party_apps_reviewed",
                     "suspicious_link_awareness","impersonation_awareness",
                     "privacy_settings_reviewed","historical_posts_reviewed","photo_metadata_awareness",
                     "tag_review_enabled","audience_review","follower_review"}:
            # For reversed controls, NO/SOMETIMES/NOT SURE indicates a gap.
            q_reverse = qid in {"mfa_enabled","unique_password","password_manager","login_alerts_enabled",
                                "recovery_reviewed","active_sessions_reviewed","third_party_apps_reviewed",
                                "suspicious_link_awareness","impersonation_awareness",
                                "privacy_settings_reviewed","historical_posts_reviewed","photo_metadata_awareness",
                                "tag_review_enabled","audience_review","follower_review"}
            triggered = (answer != "YES") if q_reverse else (answer == "YES")
        else:
            triggered = answer in {"YES", "OFTEN", "ALWAYS", "PUBLIC"}
        if triggered:
            category, title, severity, description = rule
            findings.append({
                "category": category,
                "finding_type": title,
                "severity": severity,
                "description": description,
                "source_question": qid
            })
    severity_order = {"CRITICAL":0,"HIGH":1,"MODERATE":2,"LOW":3}
    findings.sort(key=lambda x: severity_order[x["severity"]])
    return findings[:20]
