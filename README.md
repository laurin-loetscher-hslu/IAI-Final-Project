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

### 3. Run the Application
```bash
make run
```

## Troubleshooting
- Ensure both backend and frontend are running
- Check that required dependencies are installed
- Verify WebSocket connection in browser console if needed

## Technologies Used

- FastAPI
- Streamlit
- WebSocket
- Python
