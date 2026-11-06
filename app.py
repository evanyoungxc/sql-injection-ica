import os
import re
import sqlite3
from flask import Flask, request, session, render_template_string, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]

DB = os.path.join(os.path.dirname(__file__), "training.db")

def get_db():
    return sqlite3.connect(f"file:{DB}?mode=ro", uri=True)

def phase():
    return session.get("phase", 1)

def sql_bypass(value):
    return bool(re.search(
        r"'\s+OR\s+(?:'([^']+)'\s*=\s*'\1'|(\d+)\s*=\s*\2)\s*--",
        value, re.I
    ))

def union_payload(value):
    return bool(re.search(
        r"'\s+UNION\s+SELECT\s+username\s*,\s*password\s+FROM\s+users"
        r"\s+WHERE\s+role\s*=\s*'admin'\s*--",
        value, re.I
    ))

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<link rel="icon" type="image/svg+xml" href="/static/favicon.svg">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Payload Injectors | SQL Injection Lab</title>

<style>
:root {
    color-scheme:dark;
    --bg:#0a1020;
    --panel:#131e30;
    --border:#29364a;
    --muted:#94a3b8;
    --accent:#3b82f6;
}
* {box-sizing:border-box}
body {
    background:radial-gradient(ellipse at 50% -15%,#182e50 0%,#0a1020 55%);
    color:#e5eaf3;
    font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
    margin:0;min-height:100vh;
}
header {
    background:rgba(12,20,36,.95);
    border-bottom:1px solid var(--border);
    padding:20px max(24px,calc((100vw - 980px)/2));
    display:flex;justify-content:space-between;align-items:center;
    gap:15px;flex-wrap:wrap;
}
.brand {display:flex;align-items:center;gap:13px}
.brand-icon {
    display:grid;place-items:center;
    width:43px;height:43px;border-radius:12px;
    background:#172a46;color:#60a5fa;font-size:26px;
}
.brand strong {display:block;font-size:15px;letter-spacing:1.1px;color:#f8fafc}
.brand small {display:block;color:#94a3b8;font-size:11px;letter-spacing:2px;margin-top:4px}
.header-tag {
    border:1px solid #34465f;border-radius:100px;
    padding:9px 14px;color:#a9c4e7;font-size:11px;
    letter-spacing:1px;font-weight:600;
}
main {max-width:860px;margin:48px auto;padding:0 20px}
.eyebrow {color:#60a5fa;font-size:12px;font-weight:700;letter-spacing:2px}
h1 {font-size:clamp(30px,5vw,43px);letter-spacing:-1.2px;margin:12px 0}
h2 {font-size:23px;letter-spacing:-.4px;margin:12px 0}
p {color:var(--muted);line-height:1.75}
.steps {display:flex;gap:12px;margin:30px 0}
.step {
    flex:1;padding:20px 12px;text-align:center;
    background:#151f30;border:1px solid var(--border);
    border-radius:12px;font-size:13px;font-weight:600;
    color:#8292aa;
}
.step.active {background:#173454;border-color:#3b82f6;color:#93c5fd}
.step.done {background:#10291f;border-color:#166534;color:#86efac}
.card {
    background:var(--panel);border:1px solid var(--border);
    border-radius:15px;padding:32px;margin-bottom:20px;
    box-shadow:0 14px 35px rgba(0,0,0,.12);
}
label {
    display:block;margin:20px 0 8px;
    font-size:12px;font-weight:700;
    letter-spacing:1px;color:#cbd5e1;
}
input {
    width:100%;background:#0b1423;color:#fff;
    border:1px solid #34445c;border-radius:9px;
    padding:15px;font-size:15px;outline:none;
    transition:border-color .2s,box-shadow .2s;
}
input:focus {border-color:#3b82f6;box-shadow:0 0 0 3px #3b82f622}
button {
    background:linear-gradient(135deg,#2563eb,#1d4ed8);
    color:white;border:0;padding:15px 24px;
    border-radius:9px;cursor:pointer;
    font-weight:700;font-size:14px;margin-top:24px;
    transition:transform .15s,filter .15s;
}
button:hover {filter:brightness(1.15);transform:translateY(-1px)}
.console {
    background:#070d18;border:1px solid #29364a;
    color:#86efac;padding:20px;border-radius:9px;
    font-family:Consolas,Monaco,monospace;
    white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.8;
}
.error {color:#fca5a5}
.success {color:#86efac}
.tag {
    color:#60a5fa;font-size:12px;
    font-weight:800;letter-spacing:1.5px;
}
footer {
    text-align:center;padding:38px 20px;
    border-top:1px solid #29364a;
    color:#64748b;font-size:12px;line-height:2.1;
}
footer strong {color:#cbd5e1;letter-spacing:1px}
@media(max-width:600px) {
    header {padding:16px}
    .header-tag {display:none}
    main {margin:28px auto}
    .steps {gap:6px}
    .step {padding:15px 5px;font-size:11px}
    .card {padding:22px}
}

.restart-form {
    display:flex;
    justify-content:flex-end;
    margin:-10px 0 20px;
}
.restart-btn {
    background:transparent;
    color:#94a3b8;
    border:1px solid #34445c;
    border-radius:8px;
    padding:10px 16px;
    font-size:13px;
    font-weight:600;
    cursor:pointer;
    margin:0;
}
.restart-btn:hover {
    background:#26354c;
    color:#fff;
    border-color:#60a5fa;
}


.lab-hint {
    margin:20px 0;
    background:#101d30;
    border:1px solid #34445c;
    border-radius:10px;
    overflow:hidden;
}
.lab-hint summary {
    padding:15px 18px;
    color:#93c5fd;
    font-size:14px;
    font-weight:600;
    cursor:pointer;
    list-style:none;
    display:flex;
    align-items:center;
    justify-content:space-between;
}
.lab-hint summary::-webkit-details-marker {
    display:none;
}
.lab-hint summary::after {
    content:"+";
    font-size:20px;
    font-weight:400;
}
.lab-hint[open] summary::after {
    content:"−";
}
.lab-hint summary:hover {
    background:#172a46;
}
.hint-content {
    padding:16px 18px;
    border-top:1px solid #34445c;
    color:#cbd5e1;
    font-size:14px;
    line-height:1.8;
}





</style>

</head>
<body>
<header>
  <div class="brand"><div class="brand-icon">⌘</div><div><strong>THE PAYLOAD INJECTORS</strong><small>SQL INJECTION LAB</small></div></div>
  <span class="header-tag">INTERACTIVE CYBERSECURITY ICA</span>

</header>
<main>
<div class="eyebrow">INTERACTIVE SECURITY CHALLENGE</div><h1>Operation Login Bypass</h1>
<p>You are a security analyst investigating a fictional employee portal.
Identify the vulnerability, bypass authentication, and retrieve the
administrator's mock credentials.</p>

<div class="steps">
  {% for n, name in [(1,'Discovery'),(2,'Authentication'),(3,'Credentials')] %}
  <div class="step {% if phase > n %}done{% elif phase == n %}active{% endif %}">
    {% if phase > n %}✓{% else %}{{ n }}{% endif %} {{ name }}
  </div>
  {% endfor %}
</div>


<form method="POST" action="/reset"
      onsubmit="return confirm('Restart the lab? All progress will be lost.');"
      class="restart-form">
    <button type="submit" class="restart-btn">
        ↻ Restart Lab
    </button>
</form>

<div class="card">
{% if phase == 1 %}
  <div class="tag">PHASE 1 · 25 POINTS</div>
  <h2>Discover the vulnerability</h2>
<details class="lab-hint">
    <summary>💡 Need a Hint?</summary>
    <div class="hint-content">SQL uses single quotes to mark text values. What happens if you enter a single quote by itself into the username field? Pay attention to database errors.</div>
</details>

  <p>The employee portal may not handle unexpected input correctly.
  Experiment with the username field to produce an unusual database response.</p>
  <form method="POST" action="/discover">
    <label>Username</label>
    <input name="username" required autocomplete="off">
    <label>Password</label>
    <input name="password" type="password" autocomplete="off">
    <button>Test Login</button>
  </form>

{% elif phase == 2 %}
  <div class="tag">PHASE 2 · 35 POINTS</div>
  <h2>Bypass authentication</h2>
<details class="lab-hint">
    <summary>💡 Need a Hint?</summary>
    <div class="hint-content">Think about how SQL combines conditions using OR. What happens if one condition is always true? You may also need to comment out the rest of the query using two hyphens.</div>
</details>

  <p>You've discovered a possible injection point. Use SQL Boolean
  logic to authenticate without knowing a legitimate password.</p>
  <form method="POST" action="/login">
    <label>Username</label>
    <input name="username" required autocomplete="off">
    <label>Password</label>
    <input name="password" type="text" autocomplete="off">
    <button>Authenticate</button>
  </form>

{% elif phase == 3 %}
  <div class="tag">PHASE 3 · 40 POINTS</div>
  <h2>Employee Directory</h2>
<details class="lab-hint">
    <summary>💡 Need a Hint?</summary>
    <div class="hint-content">UNION SELECT combines results from two queries. Try selecting username and password from the users table, filtering for the admin role. Remember to handle the original quotation marks.</div>
</details>

  <p>Authentication bypass successful. The directory's search function
  may also be vulnerable. Recover the fictional administrator credentials
  using a UNION-based SQL injection.</p>
  <p>Available training table: <code>users(username, password, role)</code></p>
  <form method="POST" action="/search">
    <label>Employee search</label>
    <input name="query" required autocomplete="off">
    <button>Search Directory</button>
  </form>

{% else %}
  <div class="tag success">ALL PHASES COMPLETE</div>
  <h2>Investigation complete!</h2>
  <h1 class="success">100 / 100 Points</h1>
  <p>You identified a simulated SQL injection vulnerability,
  bypassed authentication, and retrieved fictional credentials.</p>
  <p><strong>Final question:</strong> How would parameterized queries
  and password hashing help prevent these vulnerabilities?</p>
{% endif %}
</div>

{% if message %}
<div class="card">
  <div class="tag">APPLICATION RESPONSE</div>
  <div class="console {% if error %}error{% endif %}">{{ message }}</div>
</div>
{% endif %}

{% if phase == 3 and credentials %}
<div class="card">
  <div class="tag success">CREDENTIALS RECOVERED</div>
  <div class="console">{{ credentials }}</div>
  <form method="POST" action="/complete">
    <button>Complete Investigation</button>
  </form>
</div>
{% endif %}

{% if phase == 4 %}
<form method="POST" action="/reset">
  <button>Restart Challenge</button>
</form>
{% endif %}
</main>
<footer><strong>THE PAYLOAD INJECTORS</strong><div>Avery West · Evan Young · Isaiah Dozier</div><div>SQL Injection · Educational simulation · Fictional data only</div></footer>
</body>
</html>
"""

def page(message="", error=False, credentials=""):
    return render_template_string(
        HTML, phase=phase(), message=message,
        error=error, credentials=credentials
    )

@app.get("/")
def index():
    return page()

@app.post("/discover")
def discover():
    if phase() != 1:
        return redirect(url_for("index"))
    username = request.form.get("username", "")[:300]
    if "'" in username:
        session["phase"] = 2
        return page(
            "SQLite OperationalError: near unexpected token: syntax error\n"
            "Potential unsafe SQL construction detected.\n"
            "Phase 1 complete. +25 points",
            True
        )
    return page("Invalid username or password. Try another input.", True)

@app.post("/login")
def login():
    if phase() != 2:
        return redirect(url_for("index"))
    username = request.form.get("username", "")[:300]
    if sql_bypass(username):
        session["phase"] = 3
        return page(
            "Authentication successful.\n"
            "Boolean condition evaluated TRUE.\n"
            "Phase 2 complete. +35 points"
        )
    return page("Authentication failed. Review your Boolean expression.", True)

@app.post("/search")
def search():
    if phase() != 3:
        return redirect(url_for("index"))
    query = request.form.get("query", "")[:300]
    if union_payload(query):
        with get_db() as db:
            record = db.execute(
                "SELECT username, password FROM users WHERE role = ?",
                ("admin",)
            ).fetchone()
        if record:
            session["found"] = True
            return page(
                "UNION query simulation successful.\n"
                "Administrator record returned.",
                credentials=f"username: {record[0]}\npassword: {record[1]}"
            )
    return page("No matching employee records.", True)

@app.post("/complete")
def complete():
    if phase() == 3 and session.get("found"):
        session["phase"] = 4
    return redirect(url_for("index"))

@app.post("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


