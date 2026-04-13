.PHONY: setup lint format test security check all clean help

PYTHON   := python3
SRC      := src
TESTS    := tests
MIN_COV  := 80

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

setup: ## Install dev dependencies and pre-commit hooks
	pip install --upgrade pip
	pip install -r requirements-dev.txt
	pre-commit install --hook-type commit-msg
	pre-commit install

format: ## Auto-format code (black + isort)
	black $(SRC)/
	isort $(SRC)/

lint: ## Run all linters (ruff, mypy, radon)
	ruff check $(SRC)/
	mypy $(SRC)/ --ignore-missing-imports
	radon cc $(SRC)/ -s -n C

test: ## Run unit tests with coverage
	pytest $(TESTS)/ \
		--cov=$(SRC) \
		--cov-report=term-missing \
		--cov-report=json:coverage.json \
		--cov-fail-under=$(MIN_COV) \
		-v

security: ## Run security scans (detect-secrets, bandit, pip-audit)
	@echo "--- Scanning for hardcoded secrets ---"
	detect-secrets scan $(SRC)/ --all-files
	@echo "--- Running Bandit code security scan ---"
	bandit -r $(SRC)/ -ll
	@echo "--- Auditing dependencies for vulnerabilities ---"
	pip-audit -r requirements.txt

check: ## CI-equivalent checks without auto-fixing (format check + lint + test + security)
	black --check --diff $(SRC)/
	isort --check-only --diff $(SRC)/
	ruff check $(SRC)/
	mypy $(SRC)/ --ignore-missing-imports
	pytest $(TESTS)/ \
		--cov=$(SRC) \
		--cov-report=term-missing \
		--cov-fail-under=$(MIN_COV) \
		-v
	detect-secrets scan $(SRC)/ --all-files
	bandit -r $(SRC)/ -ll
	pip-audit -r requirements.txt

all: format lint test security ## Run everything (format + lint + test + security)

clean: ## Remove generated artefacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete
	rm -f coverage.xml coverage.json .coverage
	rm -rf htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/
