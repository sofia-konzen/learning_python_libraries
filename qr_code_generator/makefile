.ONESHELL:  # makes all commands within a rule to be executed in same shell
.SILENT:

VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python3  # this is only really necessary on old systems
PIP = $(VENV_DIR)/bin/pip         # that wouldn't recognize .oneshell

$(VENV_DIR)/bin/activate:
	python3 -m venv "$(VENV_DIR)"
	$(PIP) install -q -r requirements.txt

install: $(VENV_DIR)/bin/activate

run: $(VENV_DIR)/bin/activate
	$(PYTHON) main.py $(ARGS)

clean:
	rm -rf __pycache__
	rm -rf */__pycache__
	rm -rf $(VENV_DIR)

.PHONY: install run clean