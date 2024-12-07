.PHONY: install run-frontend run-backend run test clean lint format help start-servers

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

# Start backend and frontend servers in the background
start-servers:
	@echo "Starting backend server..."
	cd $(BACKEND_DIR) && uvicorn chat_server:app --reload & echo $$! > backend_server.pid
	@echo "Waiting for backend server to start..."
	sleep 5 # Adjust if server takes longer to start

# Stop backend server
start-servers:
	@echo "Starting backend server..."
	@if lsof -i :8000 | grep LISTEN; then kill -9 $(shell lsof -t -i :8000); fi
	cd $(BACKEND_DIR) && uvicorn chat_server:app --reload & echo $$! > backend_server.pid
	@echo "Waiting for backend server to start..."
	sleep 5 # Adjust if server takes longer to start

# Run all tests
# Run all tests
test: start-servers
	@echo "Running tests..."
	PYTHONPATH=$(BACKEND_DIR) $(PYTHON) -m pytest $(BACKEND_DIR)/tests || { make stop-servers; exit 1; }
	@make stop-servers


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



# Help target
help:
	@echo "Available targets:"
	@echo "  install      - Install project dependencies"
	@echo "  run          - Run both frontend and backend"
	@echo "  run-frontend - Run Streamlit frontend"
	@echo "  run-backend  - Run FastAPI backend"
	@echo "  start-servers - Start backend and frontend servers in the background"
	@echo "  stop-servers - Stop backend server"
	@echo "  test         - Run all tests"
	@echo "  typecheck    - Run type checking"
	@echo "  lint         - Run code linter"
	@echo "  format       - Format code with black and isort"
	@echo "  clean        - Remove cache and temporary files"
	@echo "  venv         - Create a virtual environment"
	@echo "  help         - Show this help message"
