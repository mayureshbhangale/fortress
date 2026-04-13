# Security Policy

## Reporting a Vulnerability

**Please do NOT open a public GitHub issue for security vulnerabilities.**

Email the maintainer directly at: `security@example.com`

Include:
- A description of the vulnerability
- Steps to reproduce it
- The potential impact
- Any suggested fix (optional)

You will receive a response within **72 hours** acknowledging the report, and a
status update within **7 days**.

## Supported Versions

| Version | Supported |
|---------|-----------|
| latest  | ✅ Yes    |
| < 1.0   | ❌ No     |

## Disclosure Policy

- Vulnerabilities will be fixed in a private branch.
- A security advisory will be published after the fix is released.
- Credit will be given to the reporter unless they prefer to remain anonymous.

## Automated Security Tooling

This repository uses the following automated tools to catch security issues:

| Tool | What it checks |
|------|---------------|
| **Dependabot** | Vulnerable dependency versions (auto-raises PRs) |
| **CodeQL** | Semantic code vulnerabilities (SQL injection, path traversal, etc.) |
| **Bandit** | Python-specific code security issues |
| **detect-secrets** | Hardcoded credentials in source code |
| **pip-audit** | Known CVEs in installed packages |
