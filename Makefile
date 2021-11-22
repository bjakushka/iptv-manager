all:
	@echo "Available targets:"
	@echo "    init   - Initialize from the scratch"
	@echo "    clean  - Return project to state before initialization"
	@echo "    test   - Run tests and critical linting"
	@echo "    lint   - Run critical and other linting"
	@echo "    run    - Start development server"

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

	@echo "\nInstalling npm-packages..."
	@npm install
	@npm run build
	@echo "Done!"

# Cleaning environment
clean:
	@echo "Cleaning..."
	@rm -rf --verbose .venv
	@rm -rf --verbose .coverage
	@rm -rf --verbose public/index.html public/assets
	@rm -rf --verbose public/assets
	@rm -rf --verbose node_modules
	@rm -rf logs/*
	@rm -rf app/__pycache__/
	@rm -rf .pytest_cache
	@printf "Done!\n\n"

# Testing
test:
	@./cli test:lint --critical && ./cli test:run

# Run code linting
lint:
	@./cli test:lint --critical && ./cli test:lint

# Shortcut for running development server
run:
	@./cli run --host=0.0.0.0 --port=8000
