async function load(){
  const r = await fetch("/api/dashboard/stats");
  const d = await r.json();
  document.getElementById("total").textContent = d.total_assessments;
  document.getElementById("avg").textContent = `${d.average_score}/100`;
  document.getElementById("high").textContent =
    (d.risk_distribution.HIGH || 0) + (d.risk_distribution.CRITICAL || 0);

  new Chart(document.getElementById("distribution"), {
    type:"bar",
    data:{labels:Object.keys(d.risk_distribution),
      datasets:[{label:"Assessments",data:Object.values(d.risk_distribution)}]},
    options:{responsive:true}
  });
  new Chart(document.getElementById("categories"), {
    type:"bar",
    data:{labels:d.average_category_scores.map(x=>x.category),
      datasets:[{label:"Average Risk",data:d.average_category_scores.map(x=>x.score)}]},
    options:{indexAxis:"y",responsive:true,scales:{x:{min:0,max:100}}}
  });
}
load();
