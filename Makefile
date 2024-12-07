.PHONY: install run-frontend run-backend run test clean lint format help

# Variables
FRONTEND_DIR := frontend
BACKEND_DIR := backend
PYTHON := python3
PIP := pip3

# Default target
all: help

# Install project dependencies
install:
	@echo "Installing project dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed successfully."

# Run frontend (Streamlit)
run-frontend:
	cd $(FRONTEND_DIR) && streamlit run chat_client.py

# Run backend (Uvicorn)
run-backend:
	cd $(BACKEND_DIR) && uvicorn chat_server:app --reload

# Run both frontend and backend in parallel
run:
	@echo "Starting backend and frontend..."
	@make -j 2 run-frontend run-backend

# Run all tests
test:
	@echo "Running tests..."
	@$(PYTHON) -m pytest $(BACKEND_DIR)/tests $(FRONTEND_DIR)/tests

# Run type checking
typecheck:
	@echo "Running type checking..."
	@$(PYTHON) -m mypy $(BACKEND_DIR) $(FRONTEND_DIR)

# Run linter
lint:
	@echo "Running linter..."
	@$(PYTHON) -m flake8 $(BACKEND_DIR) $(FRONTEND_DIR)

# Format code
format:
	@echo "Formatting code..."
	@$(PYTHON) -m black $(BACKEND_DIR) $(FRONTEND_DIR)
	@$(PYTHON) -m isort $(BACKEND_DIR) $(FRONTEND_DIR)

# Clean up cache and temporary files
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +

# Create virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv venv
	@echo "Activate the virtual environment with: source venv/bin/activate"

# Help target
help:
	@echo "Available targets:"
	@echo "  install     - Install project dependencies"
	@echo "  run         - Run both frontend and backend"
	@echo "  run-frontend - Run Streamlit frontend"
	@echo "  run-backend  - Run FastAPI backend"
	@echo "  test        - Run all tests"
	@echo "  typecheck   - Run type checking"
	@echo "  lint        - Run code linter"
	@echo "  format      - Format code with black and isort"
	@echo "  clean       - Remove cache and temporary files"
	@echo "  venv        - Create a virtual environment"
	@echo "  help        - Show this help message"
