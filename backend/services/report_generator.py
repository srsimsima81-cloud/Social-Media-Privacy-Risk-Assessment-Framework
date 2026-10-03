from html import escape

def generate_html_report(record):
    categories = record["category_scores"]
    findings = record["findings"]
    recommendations = record["recommendations"]
    cat_rows = "".join(
        f"<tr><td>{escape(k)}</td><td>{v:.1f}/100</td></tr>"
        for k, v in categories.items()
    )
    finding_rows = "".join(
        f"<tr><td>{escape(f['severity'])}</td><td>{escape(f['finding_type'])}</td><td>{escape(f['description'])}</td></tr>"
        for f in findings
    )
    rec_rows = "".join(
        f"<li><strong>{escape(r['priority'])}:</strong> {escape(r['recommendation'])}</li>"
        for r in recommendations
    )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Privacy Risk Assessment Report</title>
<style>
body{{font-family:Arial,sans-serif;max-width:950px;margin:40px auto;padding:0 20px;color:#1f2937}}
h1,h2{{color:#111827}} .score{{font-size:44px;font-weight:700}} table{{width:100%;border-collapse:collapse;margin:16px 0}}
th,td{{border:1px solid #d1d5db;padding:10px;text-align:left}} th{{background:#f3f4f6}}
.badge{{display:inline-block;padding:6px 10px;border-radius:999px;background:#e5e7eb}}
.note{{background:#fff7ed;padding:14px;border-left:4px solid #f97316}}
</style></head><body>
<h1>Social Media Privacy Risk Assessment</h1>
<p><strong>Assessment ID:</strong> {escape(record['assessment_id'])}</p>
<p><strong>Date:</strong> {escape(record['created_at'])}</p>
<div class="score">{record['overall_score']:.1f}/100</div>
<p><span class="badge">{escape(record['risk_level'])}</span></p>
<h2>Category Scores</h2><table><tr><th>Category</th><th>Risk</th></tr>{cat_rows}</table>
<h2>Top Findings</h2><table><tr><th>Severity</th><th>Finding</th><th>Description</th></tr>{finding_rows}</table>
<h2>Recommendations</h2><ul>{rec_rows}</ul>
<h2>Privacy Checklist</h2><p>Review the project's checklist before sharing information publicly.</p>
<div class="note"><strong>Educational disclaimer:</strong> This framework estimates exposure/risk from self-reported privacy practices.
It is not a guarantee that an account will or will not be compromised. Scores, weights and thresholds are educational assumptions
and should be validated before professional risk decisions.</div>
</body></html>"""
