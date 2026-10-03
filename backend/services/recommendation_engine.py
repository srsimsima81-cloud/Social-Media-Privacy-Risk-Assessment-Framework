RECOMMENDATIONS = {
    "Public phone number": ("Limit phone-number visibility where possible.", "IMMEDIATE"),
    "Public personal email": ("Limit public visibility of personal email; use platform privacy controls.", "IMPORTANT"),
    "Public full birthday": ("Avoid exposing the full birth date publicly; consider showing only less precise information if needed.", "IMPORTANT"),
    "Home-related information exposed": ("Remove or restrict home-related details from public content.", "IMMEDIATE"),
    "Workplace exposure": ("Review whether workplace information needs to be public.", "GOOD PRACTICE"),
    "Education exposure": ("Review education visibility and disclose only what is necessary.", "GOOD PRACTICE"),
    "Family/relationship exposure": ("Reduce unnecessary family or relationship details in public profiles.", "IMPORTANT"),
    "Public location exposure": ("Avoid publicly broadcasting current location unless intentionally needed.", "IMMEDIATE"),
    "Real-time check-ins": ("Disable or limit public real-time check-ins.", "IMMEDIATE"),
    "Geotagging": ("Review geotagging before public sharing and remove location metadata when appropriate.", "IMPORTANT"),
    "Travel-plan exposure": ("Avoid public real-time travel plans; consider posting after leaving a location.", "IMMEDIATE"),
    "Repeated location patterns": ("Avoid posting enough repeated location context to reveal routines.", "IMPORTANT"),
    "Work/study location exposure": ("Limit public information that reveals routine work/study locations.", "IMPORTANT"),
    "Public post exposure": ("Use audience controls and review who can see future posts.", "IMPORTANT"),
    "Public photo exposure": ("Review photo audience settings and remove unnecessary public visibility.", "GOOD PRACTICE"),
    "Sensitive visual context": ("Check photos for documents, screens, badges, IDs, or family details before publishing.", "IMMEDIATE"),
    "Historical public posts": ("Review and restrict old public posts.", "IMPORTANT"),
    "Unknown connection requests": ("Verify unfamiliar profiles before accepting requests.", "IMMEDIATE"),
    "Public connections": ("Restrict visibility of connections where platform controls allow it.", "IMPORTANT"),
    "Unrestricted tagging": ("Enable tag approval/review and limit who can tag you.", "IMPORTANT"),
    "Unknown mentions": ("Limit mentions from unknown accounts where possible.", "IMPORTANT"),
    "Automatic tagged content": ("Require approval before tagged content appears on your profile.", "IMPORTANT"),
    "MFA disabled": ("Enable multi-factor authentication using the strongest supported method available.", "IMMEDIATE"),
    "Password uniqueness concern": ("Use a unique, strong password for the account.", "IMMEDIATE"),
    "Password management gap": ("Consider a reputable password manager to support unique passwords.", "IMPORTANT"),
    "Login alerts disabled": ("Enable login/security alerts where available.", "IMPORTANT"),
    "Recovery settings not reviewed": ("Review account recovery methods and keep them current.", "IMPORTANT"),
    "Active sessions not reviewed": ("Review active sessions/devices and sign out of anything unfamiliar.", "IMMEDIATE"),
    "Password reuse": ("Replace reused passwords with unique credentials.", "IMMEDIATE"),
    "Apps not reviewed": ("Review connected applications regularly and remove unnecessary access.", "IMPORTANT"),
    "Unused integrations": ("Revoke unused integrations using the platform's account settings.", "IMPORTANT"),
    "Unnecessary app permissions": ("Apply least privilege: remove app permissions that are not required.", "IMMEDIATE"),
    "Old social sign-in connections": ("Review old 'Sign in with social account' connections.", "IMPORTANT"),
    "Unexpected-link awareness gap": ("Verify unexpected links through an independent route before opening.", "IMMEDIATE"),
    "Verification-code sharing": ("Never share verification/security codes with unexpected contacts.", "IMMEDIATE"),
    "Suspicious DM response": ("Treat unexpected DMs requesting information or action as untrusted until verified.", "IMMEDIATE"),
    "Suspicious giveaway exposure": ("Avoid suspicious prize/giveaway links and verify independently.", "IMPORTANT"),
    "Old active accounts": ("Close or secure unused accounts and review their public content.", "IMPORTANT"),
    "Public comment history": ("Review old public comments and remove unnecessary exposure where appropriate.", "GOOD PRACTICE"),
    "Privacy settings not reviewed": ("Schedule periodic privacy-setting reviews.", "IMMEDIATE"),
    "Historical content not reviewed": ("Review historical public content periodically.", "IMPORTANT"),
    "Photo metadata awareness gap": ("Check metadata/privacy implications before public image sharing.", "GOOD PRACTICE"),
}

def generate_recommendations(findings):
    result = []
    seen = set()
    for finding in findings:
        key = finding["finding_type"]
        if key in RECOMMENDATIONS and key not in seen:
            recommendation, priority = RECOMMENDATIONS[key]
            result.append({
                "finding_type": key,
                "recommendation": recommendation,
                "priority": priority
            })
            seen.add(key)
    priority_order = {"IMMEDIATE":0, "IMPORTANT":1, "GOOD PRACTICE":2}
    result.sort(key=lambda x: priority_order[x["priority"]])
    return result
