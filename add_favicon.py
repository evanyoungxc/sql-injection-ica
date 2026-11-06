from pathlib import Path

tag = '<link rel="icon" type="image/svg+xml" href="/static/favicon.svg">'

for filename in ["app.py", "casino.html"]:
    path = Path(filename)
    source = path.read_text()

    if tag in source:
        print(f"{filename}: already configured")
        continue

    if "<head>" not in source:
        print(f"{filename}: <head> not found, skipped")
        continue

    source = source.replace("<head>", "<head>\n" + tag, 1)
    path.write_text(source)
    print(f"{filename}: favicon added")
