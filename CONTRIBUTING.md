# Contributing

Thanks for taking the time to contribute! Here's everything you need to know.

## Workflow

1. **Fork** the repository and create a branch from `main`:
   ```bash
   git checkout -b feat/my-feature
   ```

2. **Set up your dev environment:**
   ```bash
   make setup
   ```

3. **Make your changes.** Write tests for every new behaviour.

4. **Run all checks locally before pushing:**
   ```bash
   make check
   ```
   This runs the exact same checks as CI. If it passes locally, it will pass in CI.

5. **Commit** using [Conventional Commits](https://www.conventionalcommits.org/):
   ```
   feat: add user authentication module
   fix: handle empty input in word_count
   docs: clarify clamp function bounds
   test: add edge cases for palindrome check
   chore: update ruff to 0.5.0
   ```
   Pre-commit hooks will reject commits that don't follow this format.

6. **Open a Pull Request** against `main`. Fill in the PR template.

## Commit types

| Type | When to use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructure, no feature/fix |
| `test` | Add or update tests |
| `chore` | Maintenance, dependency updates |
| `perf` | Performance improvement |
| `ci` | CI/CD changes |

## CI requirements

All of these must pass before a PR can be merged:

- ✏️ Black formatting
- 📦 isort import sorting
- 🔎 Ruff linting
- 🔬 MyPy type checking
- 🔀 Cyclomatic complexity ≤ 10
- 📏 Function length ≤ 50 lines
- 🧪 Test coverage ≥ 80%
- 🔑 No hardcoded secrets
- 🔐 No high/medium Bandit findings
- 📦 No vulnerable dependencies
