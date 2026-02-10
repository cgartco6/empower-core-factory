Set-ExecutionPolicy Bypass -Force

winget install Python.Python.3.11 --silent
winget install Docker.DockerDesktop --silent
winget install Git.Git --silent

python -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn reportlab

Write-Host "Empower Core Factory installed on Windows"
