let questions = [];

const form = document.getElementById("assessmentForm");
const progress = document.getElementById("progress");

async function loadQuestions(){
  // The question catalog is mirrored client-side for a simple static frontend.
  // Values are deliberately limited to privacy indicators.
  const response = await fetch("/api/privacy-checklist");
  if (!response.ok) throw new Error("Unable to initialize");
  renderQuestions();
}

const QUESTION_DATA = [
["profile_visibility","Profile Visibility","Is your social-media profile publicly visible?",["PUBLIC","FRIENDS","PRIVATE"]],
["search_engine_visibility","Profile Visibility","Can your profile be discovered by search engines?",["YES","NO","SOMETIMES","NOT SURE"]],
["follower_list_public","Profile Visibility","Is your follower/following list visible to people you do not know?",["YES","NO","SOMETIMES","NOT SURE"]],
["friends_list_public","Profile Visibility","Is your friends/connections list publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["phone_public","Personal Information","Is your phone number publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["email_public","Personal Information","Is your personal email publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["birthday_public","Personal Information","Is your full birth date publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["home_info_public","Personal Information","Do your public posts reveal home-related information?",["YES","NO","SOMETIMES","NOT SURE"]],
["workplace_public","Personal Information","Is your workplace publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["education_public","Personal Information","Is your school/college or education history publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["relationship_public","Personal Information","Are family or relationship details publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["location_public","Location Privacy","Do you publicly share your current/general location?",["YES","NO","SOMETIMES","NOT SURE"]],
["realtime_checkins","Location Privacy","Do you use public real-time check-ins?",["YES","NO","SOMETIMES","NOT SURE"]],
["geotagging","Location Privacy","Do you regularly publish geotagged content?",["YES","NO","SOMETIMES","NOT SURE"]],
["travel_posts","Location Privacy","Do you post travel plans before or during a trip?",["YES","NO","SOMETIMES","NOT SURE"]],
["frequent_location_patterns","Location Privacy","Could repeated posts reveal a routine location pattern?",["YES","NO","SOMETIMES","NOT SURE"]],
["work_location_public","Location Privacy","Can public content reveal where you usually work or study?",["YES","NO","SOMETIMES","NOT SURE"]],
["posts_public","Posts & Content","Are many of your posts publicly visible?",["YES","NO","SOMETIMES","NOT SURE"]],
["photos_public","Posts & Content","Are personal photos commonly visible to the public?",["YES","NO","SOMETIMES","NOT SURE"]],
["documents_in_photos","Posts & Content","Have photos ever shown documents, screens, badges, or other sensitive context?",["YES","NO","SOMETIMES","NOT SURE"]],
["old_public_posts","Posts & Content","Do old public posts remain available without periodic review?",["YES","NO","SOMETIMES","NOT SURE"]],
["audience_review","Posts & Content","Do you review the audience before publishing sensitive-context posts?",["YES","NO","SOMETIMES","NOT SURE"]],
["unknown_connections","Friends / Followers","Do you accept connection/follow requests from unfamiliar people?",["NEVER","RARELY","SOMETIMES","OFTEN","ALWAYS"]],
["follower_review","Friends / Followers","Do you periodically review followers/connections?",["YES","NO","SOMETIMES","NOT SURE"]],
["public_connections","Friends / Followers","Can unknown users easily see your connections?",["YES","NO","SOMETIMES","NOT SURE"]],
["tag_review_enabled","Tagging & Mentions","Is tag review enabled before tags appear on your profile?",["YES","NO","SOMETIMES","NOT SURE"]],
["anyone_can_tag","Tagging & Mentions","Can anyone tag you without approval?",["YES","NO","SOMETIMES","NOT SURE"]],
["unknown_mentions","Tagging & Mentions","Can unknown users mention your account?",["YES","NO","SOMETIMES","NOT SURE"]],
["auto_tagged_posts","Tagging & Mentions","Can tagged posts appear automatically on your profile?",["YES","NO","SOMETIMES","NOT SURE"]],
["mfa_enabled","Account Security","Is multi-factor authentication (MFA) enabled?",["YES","NO","SOMETIMES","NOT SURE"]],
["unique_password","Account Security","Do you use a unique password for the account?",["YES","NO","SOMETIMES","NOT SURE"]],
["password_manager","Account Security","Do you use a password manager or another secure method to manage unique passwords?",["YES","NO","SOMETIMES","NOT SURE"]],
["login_alerts_enabled","Account Security","Are login/security alerts enabled?",["YES","NO","SOMETIMES","NOT SURE"]],
["recovery_reviewed","Account Security","Have you reviewed account recovery methods recently?",["YES","NO","SOMETIMES","NOT SURE"]],
["active_sessions_reviewed","Account Security","Have you reviewed active sessions/devices recently?",["YES","NO","SOMETIMES","NOT SURE"]],
["password_reuse_reported","Account Security","Do you reuse this password on other services?",["YES","NO","SOMETIMES","NOT SURE"]],
["third_party_apps_reviewed","Third-Party Apps","Have you reviewed connected third-party applications recently?",["YES","NO","SOMETIMES","NOT SURE"]],
["unused_apps_connected","Third-Party Apps","Do you have unused integrations connected?",["YES","NO","SOMETIMES","NOT SURE"]],
["unnecessary_permissions","Third-Party Apps","Do connected apps have permissions you no longer need?",["YES","NO","SOMETIMES","NOT SURE"]],
["social_signin_connections","Third-Party Apps","Do you have old 'Sign in with social account' connections you have not reviewed?",["YES","NO","SOMETIMES","NOT SURE"]],
["suspicious_link_awareness","Social Engineering","Do you verify unexpected links before opening them?",["YES","NO","SOMETIMES","NOT SURE"]],
["verification_code_sharing","Social Engineering","Have you ever shared a verification/security code with someone who contacted you unexpectedly?",["YES","NO","SOMETIMES","NOT SURE"]],
["suspicious_dm_response","Social Engineering","Do you respond to unexpected DMs requesting information or action?",["YES","NO","SOMETIMES","NOT SURE"]],
["impersonation_awareness","Social Engineering","Do you verify an account through an independent channel when impersonation is suspected?",["YES","NO","SOMETIMES","NOT SURE"]],
["giveaway_awareness","Social Engineering","Do you engage with suspicious giveaways or prize links?",["YES","NO","SOMETIMES","NOT SURE"]],
["old_accounts","Digital Footprint","Do old/unused social accounts remain active?",["YES","NO","SOMETIMES","NOT SURE"]],
["public_comments","Digital Footprint","Do you have a large history of public comments?",["YES","NO","SOMETIMES","NOT SURE"]],
["privacy_settings_reviewed","Digital Footprint","Have you reviewed privacy settings recently?",["YES","NO","SOMETIMES","NOT SURE"]],
["historical_posts_reviewed","Digital Footprint","Have you reviewed historical public posts recently?",["YES","NO","SOMETIMES","NOT SURE"]],
["photo_metadata_awareness","Digital Footprint","Do you check privacy implications of image metadata before public sharing?",["YES","NO","SOMETIMES","NOT SURE"]]
];

function renderQuestions(){
  let html = "";
  let last = "";
  QUESTION_DATA.forEach(([id,cat,label,opts],i)=>{
    if(cat!==last){ html += `<h2>${cat}</h2>`; last=cat; }
    html += `<div class="question">
      <label class="title" for="${id}">${i+1}. ${label}</label>
      <div class="choices">`;
    opts.forEach((opt,j)=>{
      const rid = `${id}_${j}`;
      html += `<label class="choice" for="${rid}">
        <input id="${rid}" type="radio" name="${id}" value="${opt}" required> ${opt}
      </label>`;
    });
    html += `</div></div>`;
  });
  form.innerHTML = html;
  questions = QUESTION_DATA;
  form.addEventListener("change", updateProgress);
  updateProgress();
}

function updateProgress(){
  const answered = new Set([...form.querySelectorAll("input:checked")].map(x=>x.name)).size;
  const pct = Math.round(answered/questions.length*100);
  progress.innerHTML = `<div style="width:${pct}%"></div>`;
}

form.addEventListener("submit", async (e)=>{
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());
  const status = document.getElementById("status");
  status.textContent = "Calculating...";
  try{
    const r = await fetch("/api/assessment",{
      method:"POST",headers:{"Content-Type":"application/json"},
      body:JSON.stringify({answers:data})
    });
    const result = await r.json();
    if(!r.ok) throw new Error(result.details?.join(", ") || result.error);
    sessionStorage.setItem("assessmentResult", JSON.stringify(result));
    sessionStorage.setItem("assessmentAnswers", JSON.stringify(data));
    status.innerHTML = `<p class="success">Assessment complete. Redirecting to results...</p>`;
    window.location.href = `/report/${result.assessment_id}`;
  }catch(err){
    status.innerHTML = `<p class="error">${err.message}</p>`;
  }
});

loadQuestions();
