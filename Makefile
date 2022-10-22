#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Docker variables
IMAGE := workflow_manager
VERSION := latest

# poetry show black2 &> /dev/null && echo "true" || echo "false"


#-----------------------------------------------------------------------------------------
# INSTALLATION
#-----------------------------------------------------------------------------------------
.PHONY: install-poetry
install-poetry: ## Download and install Poetry
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) -

.PHONY: uninstall-poetry
uninstall-poetry: ## Uninstall Poetry
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) - --uninstall

.PHONY: install-pyinstaller
install-pyinstaller: ## Download and install PyInstaller
	poetry add pyinstaller@latest pillow@latest

.PHONY: remove-pyinstaller
remove-pyinstaller: ## Uninstall PyInstaller
	poetry add pyinstaller@latest pillow@latest

.PHONY: install-pre-commit-hooks
install-pre-commit-hooks: ## Install Pre-Commit Git Hooks
	poetry run pre-commit install

.PHONY: install-pyqt5
install-pyqt5: ## Install PyQt5
	poetry add PyQt5@latest

#-----------------------------------------------------------------------------------------
# INSTALL/UPDATE DEPENDENCIES/REQUIREMENTS
#-----------------------------------------------------------------------------------------

.PHONY: install
install: ## Install Project Dependecies/Requirements from Poetry
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n
	-poetry run mypy --install-types --non-interactive ./

.PHONY: update-dev-deps
update-dev-deps: ## Update dev dependecies to @latest version
	poetry add -D bandit@latest darglint@latest "isort[colors]@latest" mypy@latest pre-commit@latest pydocstyle@latest pylint@latest pytest@latest pyupgrade@latest safety@latest coverage@latest coverage-badge@latest pytest-html@latest pytest-cov@latest
	poetry add -D --allow-prereleases black@latest

#-----------------------------------------------------------------------------------------
# ORIGINAL INSTALLATION HOOKS
#-----------------------------------------------------------------------------------------
.PHONY: poetry-download
poetry-download: install-poetry ## Download and install Poetry

.PHONY: pre-commit-install
pre-commit-install: install-pre-commit-hooks ## Install Pre-Commit Git Hooks

#-----------------------------------------------------------------------------------------
# Linting, Formatting, TypeCheck
#-----------------------------------------------------------------------------------------
.PHONY: lint
lint: test check-codestyle mypy check-safety ## Lint, Format, Check Types, Check Safety

.PHONY: formatting
formatting: codestyle ## Apply Formatting via PyUpgrade, ISort, Black.

.PHONY: codestyle
codestyle: ## Apply Formatting via PyUpgrade, ISort, Black.
	poetry run pyupgrade --exit-zero-even-if-changed --py310-plus **/*.py
	poetry run isort --settings-path pyproject.toml ./
	poetry run black --config pyproject.toml ./

.PHONY: check-codestyle
check-codestyle: ## Check Formatting via ISort, Black, darglint.
	poetry run isort --diff --check-only --settings-path pyproject.toml ./
	poetry run black --diff --check --config pyproject.toml ./
	poetry run darglint --verbosity 2 workflow_manager tests

.PHONY: check-safety
check-safety: ## Check Securty & Safty via Bandit, Safety.
	poetry check
	poetry run safety check --full-report
	poetry run bandit -ll --recursive workflow_manager tests

.PHONY: mypy
mypy: ## Typechecking via MyPy
	poetry run mypy --config-file pyproject.toml ./


#-----------------------------------------------------------------------------------------
# TESTS
#-----------------------------------------------------------------------------------------
.PHONY: tests
tests: test ## Run Tests & Coverage

.PHONY: test
test: ## Run Tests & Coverage
	PYTHONPATH=$(PYTHONPATH) poetry run pytest -c pyproject.toml --cov-report=html --cov=workflow_manager tests/
	poetry run coverage-badge -o assets/images/coverage.svg -f


#-----------------------------------------------------------------------------------------
# BUILDS
#-----------------------------------------------------------------------------------------
.PHONY: build-package
build-package: ## Build as Package
	poetry build

.PHONY: build-pyinstaller-linux
build-pyinstaller-linux: ## Build Linux Executable
	pyinstaller $(IMAGE)/__main__.py \
		--clean \
		--onefile \
		--windowed \
		--paths=./$(IMAGE) \
		--icon=./$(IMAGE)/resources/images/icon.png \
		--workpath=./build_linux \
		--distpath=./dist_linux

.PHONY: build-pyinstaller-win
build-pyinstaller-win: ## Build Windows Executable
	pyinstaller $(IMAGE)/__main__.py \
		--clean \
		--onefile \
		--windowed \
		--paths=./$(IMAGE) \
		--icon=./$(IMAGE)/resources/images/icon.png \
		--workpath=./build_win \
		--distpath=./dist_win

.PHONY: build-pyqt5-resources
build-pyqt5-resources: ## Build PyQt5 Resources File
	pyrcc5 $(PYTHONPATH)/assets/ui/resources.qrc -o $(PYTHONPATH)/$(IMAGE)/resources_rc.py

.PHONY: build-pyqt5-ui
build-pyqt5-ui: ## Build PyQt5 QtDesigner UI File
	pyuic5 -x $(PYTHONPATH)/assets/ui/pyqt5_ui.ui -o $(PYTHONPATH)/$(IMAGE)/pyqt5_ui.py  

.PHONY: build-desktop-file
build-desktop-file: ## Build .desktop File
	echo "[Desktop Entry]\n"\
		"Name=workflow_manager\n"\
		"Icon=$(PYTHONPATH)/$(IMAGE)/resources/images/icon.png\n"\
		"Type=Application\n"\
		"Exec=$(PYTHONPATH)/dist_linux/$(IMAGE)\n"\
		"Terminal=false" > "$(PYTHONPATH)/dist_linux/$(IMAGE).desktop"

.PHONY: install-desktop-file
install-desktop-file: ## Install .desktop shortcut for user
	desktop-file-install --dir=~/.local/share/applications "$(PYTHONPATH)/dist_linux/$(IMAGE).desktop"
	update-desktop-database ~/.local/share/applications

.PHONY: update-desktop-database
update-desktop-database: ## Updates Linux database of .desktop shortcuts
	update-desktop-database ~/.local/share/applications


#-----------------------------------------------------------------------------------------
# DOCKER
#-----------------------------------------------------------------------------------------
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION=0.0.1
.PHONY: docker-build
docker-build: ## Build a docker image from Dockerfile
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

# Example: make docker-remove VERSION=latest
# Example: make docker-remove IMAGE=some_name VERSION=0.0.1
.PHONY: docker-remove
docker-remove: ## Remove Docker Image
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)


#-----------------------------------------------------------------------------------------
# CLEANUP
#-----------------------------------------------------------------------------------------
.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove ## Complete Cleanup

.PHONY: pycache-remove
pycache-remove: ## Clean PyCache
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove: ## Clean .DS_Store
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove: ## Clean .mypy_cache
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove: ## Clean ipynb_checkpoints
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove: ## Clean pytest_cache
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove: ## Clean Builds
	rm -rf build/
	rm -rf build_linux/
	rm -rf build_win/


#-----------------------------------------------------------------------------------------
# HELP
#-----------------------------------------------------------------------------------------
.PHONY: help
help: ## Self-documented Makefile
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
