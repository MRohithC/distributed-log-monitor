# Distributed Log Monitor

A simple distributed log monitoring system built using Flask and SQLite.
This project simulates multiple services sending logs to central server, wgere logs are stored, viewed and filtered

## Features
- Collect logs from multiple services
- Store logs in a central database
- View logs via API
- Filter logs by:
  - Service name
  - Log level (INFO, ERROR, WARNING)
- Simple and lightweight backend using Flask

## Tech Stack
- Python
- Flask
- SQLite

## How It Works

Multiple services send logs like this:

```json
{
  "service": "auth-service",
  "level": "ERROR",
  "message": "Invalid password"
}

## How to Run

```bash
git clone <repo-url>
cd distributed-log-monitor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
