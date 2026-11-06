# SQL Injection ICA — The Payload Injectors

An interactive, browser-based cybersecurity lab designed to demonstrate SQL injection vulnerabilities through three progressive challenges.

**Live Demo:** https://ica.eyoungcyber.com

**Group Members:** Avery West, Evan Young, Isaiah Dozier

## Project Overview

This project was developed as an in-class cybersecurity activity to help students understand how SQL injection can affect web applications.

Participants progress through three challenges involving error-based discovery, authentication bypass, and credential extraction. Each phase builds on concepts introduced in the previous challenge.

The application simulates vulnerable SQL behavior in a controlled environment using fictional data. Students can experiment with SQL injection syntax without executing arbitrary SQL queries against a production database.

## Challenge Phases

### Phase 1 — Vulnerability Discovery

Students investigate an employee login form to identify potential SQL injection vulnerabilities.

**Learning objectives:**
- Understand how web applications handle user input.
- Recognize SQL syntax errors as potential indicators of insecure query construction.
- Identify why input validation and parameterized queries matter.

### Phase 2 — Authentication Bypass

Students construct a SQL injection payload that manipulates Boolean logic to simulate bypassing authentication.

**Learning objectives:**
- Understand SQL `OR` conditions.
- Explore how SQL comments can alter query behavior.
- Recognize the risks of constructing authentication queries using untrusted input.

### Phase 3 — Credential Extraction

Students use a simulated `UNION SELECT` injection to retrieve fictional administrator credentials.

**Learning objectives:**
- Understand how SQL `UNION` combines query results.
- Identify the risks of excessive database permissions.
- Explore how injection vulnerabilities can expose sensitive information.

## Features

- Three sequential SQL injection challenges
- Interactive login and employee search interfaces
- Progressive challenge unlocking
- Expandable hints for each phase
- Score tracking and completion screen
- Restart Lab functionality
- Responsive cybersecurity-themed interface
- Custom favicon and project branding
- Fictional SQLite database for training

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic |
| Flask | Web application framework |
| SQLite | Fictional training database |
| HTML / CSS | User interface |
| Gunicorn | Production WSGI application server |
| Nginx | Reverse proxy |
| AWS EC2 | Cloud hosting |
| Let's Encrypt | HTTPS certificates |
| Ubuntu Linux | Server operating system |
| Git / GitHub | Version control |

## Architecture

The application is hosted on an AWS EC2 Ubuntu instance.

```text
Student Browser
      |
      | HTTPS
      v
Nginx Reverse Proxy
      |
      v
Gunicorn Application Server
      |
      v
Flask Web Application
      |
      v
SQL Injection Simulator
      |
      v
SQLite Training Database
```

Nginx handles HTTPS traffic and forwards requests to Gunicorn, which serves the Flask application.

The application recognizes specific SQL injection patterns and simulates their effects. Database access is performed separately using controlled queries.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/evanyoungxc/sql-injection-ica.git
cd sql-injection-ica
```

### 2. Create a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install Flask gunicorn
```

### 4. Initialize the training database

```bash
python init_db.py
```

### 5. Configure the Flask secret key

```bash
export FLASK_SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
```

### 6. Start the application

```bash
gunicorn --bind 127.0.0.1:8000 app:app
```

Open `http://127.0.0.1:8000` in a browser on the same machine.

## Security Considerations

This project is intended exclusively for educational cybersecurity training.

- All user accounts and credentials are fictional.
- SQL injection outcomes are simulated rather than executed as unrestricted database queries.
- The training database is isolated from real user information.
- Database queries use controlled access patterns.
- The deployed application uses HTTPS.
- The application is designed to demonstrate vulnerabilities without exposing a genuinely exploitable production database.

**Important:** The simulator is not a substitute for testing SQL injection against a real application in an authorized environment.

## Educational Outcomes

By completing the lab, students gain practical familiarity with:

- SQL injection fundamentals
- Error-based vulnerability discovery
- Boolean-based authentication bypass
- `UNION SELECT` injection concepts
- Secure database query construction
- The importance of least-privilege database access

## Authors

**The Payload Injectors**

- Avery West
- Evan Young
- Isaiah Dozier

Developed as an interactive cybersecurity in-class activity.

---

*For educational and authorized security training only.*
