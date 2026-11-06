from pathlib import Path

path = Path("app.py")
source = path.read_text()

button = """
<form method="POST" action="/reset"
      onsubmit="return confirm('Restart the lab? All progress will be lost.');"
      class="restart-form">
    <button type="submit" class="restart-btn">
        ↻ Restart Lab
    </button>
</form>
"""

# Add restart button below the phase progress indicator
target = '<div class="card">\n{% if phase == 1 %}'

if 'class="restart-form"' not in source:
    if target not in source:
        raise SystemExit("Could not find the phase section. No changes made.")
    source = source.replace(
        target,
        button + '\n' + target,
        1
    )

# Add button styling
css = """
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
"""

if ".restart-btn {" not in source:
    source = source.replace(
        "</style>",
        css + "\n</style>",
        1
    )

path.write_text(source)
print("Restart Lab button added successfully.")
