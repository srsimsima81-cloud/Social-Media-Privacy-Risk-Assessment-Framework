
const answers = JSON.parse(sessionStorage.getItem("assessmentAnswers") || "null");
const current = JSON.parse(sessionStorage.getItem("assessmentResult") || "null");
const state = document.getElementById("state");
const form = document.getElementById("simForm");

const changes = [
  ["phone_public","Make phone visibility private","NO"],
  ["birthday_public","Hide full birthday","NO"],
  ["location_public","Stop public location sharing","NO"],
  ["travel_posts","Stop public travel-plan sharing","NO"],
  ["unknown_connections","Reject unfamiliar connection requests","NEVER"],
  ["tag_review_enabled","Enable tag review","YES"],
  ["mfa_enabled","Enable MFA","YES"],
  ["login_alerts_enabled","Enable login alerts","YES"],
  ["third_party_apps_reviewed","Review connected apps","YES"],
  ["historical_posts_reviewed","Review historical public posts","YES"],
  ["privacy_settings_reviewed","Review privacy settings","YES"]
];

if (!answers || !current) {
  state.textContent = "No assessment is available in this browser session. Complete an assessment first.";
} else {
  state.innerHTML = `Current score: <strong>${current.overall_score}/100</strong> (${current.risk_level})`;
  form.innerHTML = changes.map(([id,label,value],i)=>`
    <div class="question">
      <label class="choice" for="change_${i}">
        <input id="change_${i}" type="checkbox" data-key="${id}" data-value="${value}">
        ${label}
      </label>
    </div>`).join("");
}

document.getElementById("simulate").addEventListener("click", async ()=>{
  if(!answers) return;
  const selected = {};
  form.querySelectorAll("input:checked").forEach(x => selected[x.dataset.key]=x.dataset.value);
  const r = await fetch("/api/assessment/simulate-improvement", {
    method:"POST", headers:{"Content-Type":"application/json"},
    body:JSON.stringify({answers,changes:selected})
  });
  const data = await r.json();
  if(!r.ok){ state.textContent = data.error || "Simulation failed"; return; }
  document.getElementById("result").innerHTML = `
    <div class="card">
      <h2>Simulation Result</h2>
      <div class="cards">
        <div class="metric"><span>Current</span><strong>${data.current_score}/100</strong><small>${data.current_level}</small></div>
        <div class="metric"><span>Simulated</span><strong>${data.simulated_score}/100</strong><small>${data.simulated_level}</small></div>
        <div class="metric"><span>Risk reduction</span><strong>${data.risk_reduction}</strong><small>points</small></div>
      </div>
      <p class="notice">${data.disclaimer}</p>
    </div>`;
});
