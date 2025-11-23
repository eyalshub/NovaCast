# Makefile for NovaCast Project

.PHONY: run install lint test docker-build docker-compose-up

# Run the FastAPI application
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Install project dependencies
install:
	pip install -r requirements.txt

# Lint the codebase
lint:
	flake8 app tests scripts

# Run tests
test:
	pytest tests

# Build Docker images
docker-build:
	docker build -f docker/Dockerfile.api -t novacast-api .
	docker build -f docker/Dockerfile.worker -t novacast-worker .

# Start services with Docker Compose
docker-compose-up:
	docker-compose up --build