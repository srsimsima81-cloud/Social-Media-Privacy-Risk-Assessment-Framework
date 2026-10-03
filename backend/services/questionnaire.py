# Privacy-preserving questionnaire.
# No question asks the user to submit the actual sensitive value.

QUESTIONS = [
    # A Profile Visibility
    {"id":"profile_visibility","category":"Profile Visibility","label":"Is your social-media profile publicly visible?","type":"choice","options":["PUBLIC","FRIENDS","PRIVATE"]},
    {"id":"search_engine_visibility","category":"Profile Visibility","label":"Can your profile be discovered by search engines?","type":"yn"},
    {"id":"follower_list_public","category":"Profile Visibility","label":"Is your follower/following list visible to people you do not know?","type":"yn"},
    {"id":"friends_list_public","category":"Profile Visibility","label":"Is your friends/connections list publicly visible?","type":"yn"},

    # B Personal Information
    {"id":"phone_public","category":"Personal Information","label":"Is your phone number publicly visible?","type":"yn"},
    {"id":"email_public","category":"Personal Information","label":"Is your personal email publicly visible?","type":"yn"},
    {"id":"birthday_public","category":"Personal Information","label":"Is your full birth date publicly visible?","type":"yn"},
    {"id":"home_info_public","category":"Personal Information","label":"Do your public posts reveal home-related information?","type":"yn"},
    {"id":"workplace_public","category":"Personal Information","label":"Is your workplace publicly visible?","type":"yn"},
    {"id":"education_public","category":"Personal Information","label":"Is your school/college or education history publicly visible?","type":"yn"},
    {"id":"relationship_public","category":"Personal Information","label":"Are family or relationship details publicly visible?","type":"yn"},

    # C Location
    {"id":"location_public","category":"Location Privacy","label":"Do you publicly share your current/general location?","type":"yn"},
    {"id":"realtime_checkins","category":"Location Privacy","label":"Do you use public real-time check-ins?","type":"yn"},
    {"id":"geotagging","category":"Location Privacy","label":"Do you regularly publish geotagged content?","type":"yn"},
    {"id":"travel_posts","category":"Location Privacy","label":"Do you post travel plans before or during a trip?","type":"yn"},
    {"id":"frequent_location_patterns","category":"Location Privacy","label":"Could repeated posts reveal a routine location pattern?","type":"yn"},
    {"id":"work_location_public","category":"Location Privacy","label":"Can public content reveal where you usually work or study?","type":"yn"},

    # D Posts & Content
    {"id":"posts_public","category":"Posts & Content","label":"Are many of your posts publicly visible?","type":"yn"},
    {"id":"photos_public","category":"Posts & Content","label":"Are personal photos commonly visible to the public?","type":"yn"},
    {"id":"documents_in_photos","category":"Posts & Content","label":"Have photos ever shown documents, screens, badges, or other sensitive context?","type":"yn"},
    {"id":"old_public_posts","category":"Posts & Content","label":"Do old public posts remain available without periodic review?","type":"yn"},
    {"id":"audience_review","category":"Posts & Content","label":"Do you review the audience before publishing sensitive-context posts?","type":"yn","reverse":True},

    # E Friends / Followers
    {"id":"unknown_connections","category":"Friends / Followers","label":"Do you accept connection/follow requests from unfamiliar people?","type":"freq"},
    {"id":"follower_review","category":"Friends / Followers","label":"Do you periodically review followers/connections?","type":"yn","reverse":True},
    {"id":"public_connections","category":"Friends / Followers","label":"Can unknown users easily see your connections?","type":"yn"},

    # F Tagging
    {"id":"tag_review_enabled","category":"Tagging & Mentions","label":"Is tag review enabled before tags appear on your profile?","type":"yn","reverse":True},
    {"id":"anyone_can_tag","category":"Tagging & Mentions","label":"Can anyone tag you without approval?","type":"yn"},
    {"id":"unknown_mentions","category":"Tagging & Mentions","label":"Can unknown users mention your account?","type":"yn"},
    {"id":"auto_tagged_posts","category":"Tagging & Mentions","label":"Can tagged posts appear automatically on your profile?","type":"yn"},

    # G Account Security
    {"id":"mfa_enabled","category":"Account Security","label":"Is multi-factor authentication (MFA) enabled?","type":"yn","reverse":True},
    {"id":"unique_password","category":"Account Security","label":"Do you use a unique password for the account?","type":"yn","reverse":True},
    {"id":"password_manager","category":"Account Security","label":"Do you use a password manager or another secure method to manage unique passwords?","type":"yn","reverse":True},
    {"id":"login_alerts_enabled","category":"Account Security","label":"Are login/security alerts enabled?","type":"yn","reverse":True},
    {"id":"recovery_reviewed","category":"Account Security","label":"Have you reviewed account recovery methods recently?","type":"yn","reverse":True},
    {"id":"active_sessions_reviewed","category":"Account Security","label":"Have you reviewed active sessions/devices recently?","type":"yn","reverse":True},
    {"id":"password_reuse_reported","category":"Account Security","label":"Do you reuse this password on other services?","type":"yn"},

    # H Third-party apps
    {"id":"third_party_apps_reviewed","category":"Third-Party Apps","label":"Have you reviewed connected third-party applications recently?","type":"yn","reverse":True},
    {"id":"unused_apps_connected","category":"Third-Party Apps","label":"Do you have unused integrations connected?","type":"yn"},
    {"id":"unnecessary_permissions","category":"Third-Party Apps","label":"Do connected apps have permissions you no longer need?","type":"yn"},
    {"id":"social_signin_connections","category":"Third-Party Apps","label":"Do you have old 'Sign in with social account' connections you have not reviewed?","type":"yn"},

    # I Social Engineering
    {"id":"suspicious_link_awareness","category":"Social Engineering","label":"Do you verify unexpected links before opening them?","type":"yn","reverse":True},
    {"id":"verification_code_sharing","category":"Social Engineering","label":"Have you ever shared a verification/security code with someone who contacted you unexpectedly?","type":"yn"},
    {"id":"suspicious_dm_response","category":"Social Engineering","label":"Do you respond to unexpected DMs requesting information or action?","type":"yn"},
    {"id":"impersonation_awareness","category":"Social Engineering","label":"Do you verify an account through an independent channel when impersonation is suspected?","type":"yn","reverse":True},
    {"id":"giveaway_awareness","category":"Social Engineering","label":"Do you engage with suspicious giveaways or prize links?","type":"yn"},

    # J Digital Footprint
    {"id":"old_accounts","category":"Digital Footprint","label":"Do old/unused social accounts remain active?","type":"yn"},
    {"id":"public_comments","category":"Digital Footprint","label":"Do you have a large history of public comments?","type":"yn"},
    {"id":"privacy_settings_reviewed","category":"Digital Footprint","label":"Have you reviewed privacy settings recently?","type":"yn","reverse":True},
    {"id":"historical_posts_reviewed","category":"Digital Footprint","label":"Have you reviewed historical public posts recently?","type":"yn","reverse":True},
    {"id":"photo_metadata_awareness","category":"Digital Footprint","label":"Do you check privacy implications of image metadata before public sharing?","type":"yn","reverse":True},
]

CATEGORIES = [
    "Profile Visibility","Personal Information","Location Privacy","Posts & Content",
    "Friends / Followers","Tagging & Mentions","Account Security","Third-Party Apps",
    "Social Engineering","Digital Footprint"
]

ALLOWED_YN = {"YES","NO","SOMETIMES","NOT SURE"}
ALLOWED_FREQ = {"NEVER","RARELY","SOMETIMES","OFTEN","ALWAYS"}
ALLOWED_VIS = {"PUBLIC","FRIENDS","PRIVATE"}
