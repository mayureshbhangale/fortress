# Fortress 🏰

> Clone once. Quality enforced forever.

A GitHub template repository for Python projects. Every pull request is
automatically checked for formatting, linting, type safety, test coverage,
code complexity, and security vulnerabilities — nothing merges to `main`
unless everything passes.

[![CI](https://github.com/your-username/fortress/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/fortress/actions/workflows/ci.yml)
[![CodeQL](https://github.com/your-username/fortress/actions/workflows/codeql.yml/badge.svg)](https://github.com/your-username/fortress/actions/workflows/codeql.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Why This Exists

LLM-generated code is fast but often sloppy: no tests, hardcoded API keys,
500-line functions, untyped parameters, and libraries with known CVEs.
This template makes quality non-negotiable. You can't merge code that fails
the checks — not because of discipline, but because the gate is automatic.

---

## What This Enforces

| Check | Tool | Why it matters |
|-------|------|----------------|
| **Formatting** | Black | Eliminates style debates. All code looks the same. |
| **Import sorting** | isort | Consistent, readable import blocks. |
| **Linting** | Ruff | Catches bugs, unused variables, bad patterns — fast. |
| **Type checking** | MyPy | Catches type mismatches before they become runtime errors. |
| **Cyclomatic complexity** | Radon | Functions with complexity > 10 have too many branches. They're hard to test and easy to break. |
| **Function length** | Custom AST | Functions over 50 lines are doing too much. Forces decomposition. |
| **Test coverage** | pytest-cov | Minimum 80% line coverage. Untested code is unknown code. |
| **Hardcoded secrets** | detect-secrets | Prevents API keys and passwords from being committed. |
| **Code security** | Bandit | Finds SQL injection, eval(), shell injection, weak crypto, and more. |
| **Dependency vulnerabilities** | pip-audit | Fails the build if any installed package has a known CVE. |
| **Semantic code analysis** | CodeQL | GitHub's deep analysis — catches entire vulnerability classes. |
| **Dependency updates** | Dependabot | Automatically raises PRs when dependencies have new versions or vulnerabilities. |

---

## CI Pipeline

```
Pull Request opened / pushed
          │
          ▼
┌─────────────────────────────────────────┐
│  Job 1: 🔍 Code Quality                │
│                                         │
│  ✏️  Black (formatting)                 │
│  📦 isort (imports)                     │
│  🔎 Ruff (linting)                      │
│  🔬 MyPy (types)                        │
│  🔀 Radon (complexity)                  │
│  📏 AST (function length)               │
│                                         │
│  All 6 checks run — even if one fails.  │
│  Developer sees ALL problems at once.   │
└──────────────────┬──────────────────────┘
                   │ (only if Job 1 passes)
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
┌───────────────┐   ┌──────────────────────┐
│ Job 2: 🧪     │   │ Job 3: 🛡️ Security   │
│ Tests +       │   │                      │
│ Coverage      │   │ 🔑 detect-secrets    │
│               │   │ 🔐 Bandit            │
│ pytest        │   │ 📦 pip-audit         │
│ ≥ 80% cov     │   │                      │
└───────────────┘   └──────────────────────┘

Jobs 2 and 3 run in PARALLEL to save time.
Both must pass before merging.
```

---

## Quick Start

### Use as a GitHub Template

1. Click **"Use this template"** → **"Create a new repository"**
2. Clone your new repo
3. Set up your dev environment:

```bash
make setup
```

4. Delete `src/example.py` and `tests/test_example.py`, then add your own code.

5. Verify everything works:

```bash
make check
```

### Manual setup (without GitHub template)

```bash
git clone https://github.com/your-username/fortress.git my-project
cd my-project
rm -rf .git && git init
make setup
```

---

## Running Checks Locally

| Command | What it does |
|---------|-------------|
| `make setup` | Install all dev dependencies + pre-commit hooks |
| `make format` | Auto-format with Black and isort |
| `make lint` | Run Ruff, MyPy, and Radon |
| `make test` | Run pytest with coverage report |
| `make security` | Run detect-secrets, Bandit, pip-audit |
| `make check` | **Everything** — mirrors CI exactly. Run before every push. |
| `make all` | format + lint + test + security (auto-fixes formatting) |
| `make clean` | Remove generated files and caches |

---

## Configuration

All thresholds are defined as environment variables at the top of `.github/workflows/ci.yml`:

```yaml
env:
  PYTHON_VERSION: "3.12"    # Python version for all CI jobs
  MIN_COVERAGE: 80          # Minimum test coverage percentage (0–100)
  MAX_COMPLEXITY: 10        # Max cyclomatic complexity per function
  MAX_FUNCTION_LENGTH: 50   # Max lines per function
  SOURCE_DIR: "src"         # Where your source code lives
  TESTS_DIR: "tests"        # Where your tests live
```

Change these values to match your project's standards.

---

## Customisation

### Adding a check

1. Add the tool to `requirements-dev.txt`
2. Add a step in `ci.yml` following the same pattern: `continue-on-error: true`, write to `$GITHUB_STEP_SUMMARY`, set a status file, check status at end
3. Add it to the summary gate step

### Removing a check

Delete the step from `ci.yml` and remove the tool from `requirements-dev.txt`.

### Adapting for a different language

Replace the Python-specific tools (Black, isort, Ruff, MyPy, Radon, Bandit) with
equivalents for your language. The CI structure (3 jobs, summary gate, parallel
security scan) works for any language.

### Adding integration tests

1. Create `tests/integration/` directory
2. Add a 4th job in `ci.yml` that needs `tests` and `security`
3. Use `services:` to spin up any required databases or services

---

## Branch Protection

After pushing to GitHub, configure branch protection on `main`:

1. Go to **Settings** → **Branches** → **Add rule**
2. Branch name pattern: `main`
3. Enable:
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging
   - Status checks: `Code Quality`, `Tests + Coverage`, `Security Scan`
   - ✅ Require conversation resolution before merging

Nothing merges without green CI.
# test
