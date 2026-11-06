from pathlib import Path

path = Path("app.py")
source = path.read_text()

source = source.replace(
    "<title>Operation Login Bypass | Cybersecurity ICA</title>",
    "<title>The Payload Injectors | SQL Injection Lab</title>"
)

source = source.replace(
    "<strong>CYBERSECURITY ICA</strong>",
    '<div class="brand"><div class="brand-icon">⌘</div>'
    '<div><strong>THE PAYLOAD INJECTORS</strong>'
    '<small>SQL INJECTION LAB</small></div></div>'
)

source = source.replace(
    '<span>OPERATION LOGIN BYPASS · 100 POINTS</span>',
    '<span class="header-tag">INTERACTIVE CYBERSECURITY ICA</span>'
)

source = source.replace(
    "<h1>Operation Login Bypass</h1>",
    '<div class="eyebrow">INTERACTIVE SECURITY CHALLENGE</div>'
    '<h1>Operation Login Bypass</h1>'
)

source = source.replace(
    '<footer>Authorized cybersecurity training · Simulated SQL behavior · Fictional data only</footer>',
    '<footer><strong>THE PAYLOAD INJECTORS</strong>'
    '<div>Avery West · Evan Young · Isaiah Dozier</div>'
    '<div>SQL Injection · Educational simulation · Fictional data only</div>'
    '</footer>'
)

style = """
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
</style>
"""

start = source.index("<style>")
end = source.index("</style>", start) + len("</style>")
source = source[:start] + style + source[end:]

path.write_text(source)
print("Website styling updated successfully.")
