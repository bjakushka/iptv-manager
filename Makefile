all:
	@echo "Available targets:"
	@echo "    init"
	@echo "    clean"
	@echo "    run"

# Initializing environment for development
init:
	@echo "Initializing virtual envrionment..."
	@python3 -m venv .venv
	@printf "Done!\n\n"

	@echo "Python version:"
	@.venv/bin/python --version
	@chmod +x ./cli

	@echo "\nInstalling requirements..."
	@.venv/bin/pip install -r requirements.txt
	@echo "Done!"

# Cleaning environment
clean:
	@echo "Cleaning..."
	@rm -rf --verbose .venv
	@rm -rf --verbose .coverage
	@rm -rf logs/*
	@rm -rf app/__pycache__/
	@printf "Done!\n\n"

# Shortcut for running development server
run:
	@./cli run --host=0.0.0.0 --port=8000
