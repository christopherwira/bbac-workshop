FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set Python Path to our root directory
ENV PYTHONPATH="${PYTHONPATH}:/workspaces/bbac-workshop"

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
