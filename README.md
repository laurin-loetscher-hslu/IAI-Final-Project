# IAI-Final-Project

# Real-Time WebSocket Chat Application

## Overview
This is a real-time chat application built using FastAPI for the backend, Streamlit for the frontend, and WebSocket for instant messaging. The application allows multiple users to connect and exchange messages in real-time.

## Project Structure
- `backend/`: Contains the FastAPI WebSocket server
- `frontend/`: Contains the Streamlit chat client
- `Makefile`: Provides convenient commands for project management

## Prerequisites
- Python 3.9+
- pyenv (recommended for Python version management)
- pip

## Setup Instructions

### 1. Create Virtual Environment
```bash
pyenv virtualenv 3.10.6 your-project-env
pyenv activate your-project-env
```
### 2. Install Dependencies
```bash
make install
```

### 3. Set Environment Variable
Ensure the `WEBSOCKET_URL` environment variable is set to the appropriate WebSocket server URL. For example:
```bash
export WEBSOCKET_URL="ws://localhost:8000/ws"
```

### 4. Run the Application
```bash
make run
```

## Makefile Commands
Here are the available commands in the `Makefile` for managing and running the project:

- **`make install`**
  Install all project dependencies.

- **`make run-frontend`**
  Run the Streamlit frontend application.

- **`make run-backend`**
  Run the FastAPI backend server.

- **`make run`**
  Run both frontend and backend in parallel.

- **`make start-servers`**
  Start backend and frontend servers in the background.
  Backend server runs with Uvicorn, and frontend runs with Streamlit.

- **`make stop-servers`**
  Stop the backend and frontend servers running in the background.

- **`make test`**
  Run all tests.
  The backend server is started and stopped automatically during testing.

- **`make clean`**
  Remove cache, temporary files, and other development artifacts (e.g., `__pycache__`, `.pyc`).

- **`make lint`**
  Run code linters to check for formatting and style issues.

- **`make format`**
  Format the codebase using `black` and `isort`.

- **`make help`**
  Display a list of available `Makefile` commands with their descriptions.

## Troubleshooting
- Ensure both backend and frontend are running
- Check that required dependencies are installed
- Verify WebSocket connection in browser console if needed

## Technologies Used

- FastAPI
- Streamlit
- WebSocket
- Python
