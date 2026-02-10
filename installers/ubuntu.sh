#!/bin/bash
sudo apt update
sudo apt install -y python3 python3-venv docker.io docker-compose git nginx

python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn reportlab

sudo systemctl enable docker
sudo systemctl start docker

echo "Empower Core Factory installed on Ubuntu 24.04"
