VENV_BIN = .venv/bin
PYTHON = $(VENV_BIN)/python3
PIP = $(VENV_BIN)/pip

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install   Install depedencies"
	@echo "  dev       Start local API server"
	@echo "  test      Run tests"
	@echo "  lint      Run linter"
	@echo "  lint_fix  Reformat code"
	@echo "  clean     Clean up all generated files"
	@echo ""

.venv:
	python3 -m venv .venv

.PHONY: install
install: .venv
	$(PIP) install -r requirements.txt

.PHONY: dev
dev:
	$(PYTHON) -m fastapi dev

.PHONY: test
test:
	$(PYTHON) -m pytest

.PHONY: lint
lint:
	$(PYTHON) -m pylint app
	$(PYTHON) -m black app --check

.PHONY: lint_fix
lint_fix:
	$(PYTHON) -m black app

.PHONY: clean
clean:
	rm -rf .venv