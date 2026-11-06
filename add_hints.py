from pathlib import Path
import re

path = Path("app.py")
source = path.read_text()

hints = {
    1: (
        "SQL uses single quotes to mark text values. "
        "What happens if you enter a single quote by itself "
        "into the username field? Pay attention to database errors."
    ),
    2: (
        "Think about how SQL combines conditions using OR. "
        "What happens if one condition is always true? "
        "You may also need to comment out the rest of "
        "the query using two hyphens."
    ),
    3: (
        "UNION SELECT combines results from two queries. "
        "Try selecting username and password from the users "
        "table, filtering for the admin role. "
        "Remember to handle the original quotation marks."
    )
}

# Avoid adding duplicate hints.
if 'class="lab-hint"' in source:
    raise SystemExit("Hints already appear to be installed.")

# Find the phase sections in the existing HTML template.
# Insert each hint immediately after its phase heading.
for phase, hint in hints.items():
    pattern = (
        r'(\{%\s*(?:if|elif)\s+phase\s*==\s*'
        + str(phase)
        + r'\s*%\}[\s\S]*?<h2[^>]*>[\s\S]*?</h2>)'
    )

    dropdown = f'''
<details class="lab-hint">
    <summary>💡 Need a Hint?</summary>
    <div class="hint-content">{hint}</div>
</details>
'''

    source, count = re.subn(
        pattern,
        lambda m: m.group(1) + dropdown,
        source,
        count=1
    )

    if count != 1:
        raise SystemExit(
            f"Could not find Phase {phase} heading. "
            "No changes saved."
        )

css = """
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
"""

if "</style>" not in source:
    raise SystemExit("CSS style block not found. No changes saved.")

source = source.replace(
    "</style>",
    css + "\n</style>",
    1
)

path.write_text(source)
print("Successfully added hints to all three phases.")
