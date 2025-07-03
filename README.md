# Module 8: FastAPI Web Calculator with CI/CD and Docker

![GitHub Actions Workflow Status](https://github.com/RoddyCodes/RPmodule8_is601/actions/workflows/test.yml/badge.svg)

This repository contains a simple web-based calculator application built using the FastAPI framework, complete with a clean frontend, Dockerization, comprehensive testing, and an automated CI/CD pipeline managed by GitHub Actions.

## DockerHub URL

You can find the Docker image for this application on Docker Hub:

[https://hub.docker.com/repository/docker/roddycodes/is601_module8/general](https://hub.docker.com/repository/docker/roddycodes/is601_module8/general)

## Project Description

This project demonstrates a robust development workflow for a web application. It features:

- A **FastAPI backend** handling arithmetic operations.
- A simple **HTML/JavaScript frontend** for user interaction.
- **Containerization** using Docker for consistent environments.
- Extensive **testing suite** covering unit, integration, and end-to-end scenarios.
- Automated **CI/CD pipeline** with GitHub Actions for continuous testing, security scanning, and deployment.
- **Enhanced logging** for better observability and debugging.

## Features

- **Basic Arithmetic Operations:** Addition, Subtraction, Multiplication, and Division.
- **Web Interface:** User-friendly calculator accessible via a web browser.
- **RESTful API:** Backend exposes endpoints for each arithmetic operation.
- **Input Validation:** Robust handling of invalid inputs (e.g., non-numeric values, division by zero).
- **Containerized Environment:** Application runs within a Docker container for portability.

## Technologies Used

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python web framework), [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- **Frontend:** HTML, JavaScript, [Jinja2Templates](https://jinja.palletsprojects.com/)
- **Containerization:** [Docker](https://www.docker.com/), [Docker Compose](https://docs.docker.com/compose/)
- **Testing:** [Pytest](https://docs.pytest.org/en/stable/), [pytest-asyncio](https://pytest-asyncio.readthedocs.io/en/latest/), [httpx](https://www.python-httpx.org/), [Playwright](https://playwright.dev/)
- **CI/CD:** [GitHub Actions](https://docs.github.com/en/actions)
- **Security Scanning:** [Trivy](https://aquasecurity.github.io/trivy/)
- **Image Registry:** [Docker Hub](https://hub.docker.com/)

## Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

- [Git](https://git-scm.com/downloads) installed.
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running (includes Docker Engine and Docker Compose).
- (Optional, for local testing outside Docker) [Python 3.10+](https://www.python.org/downloads/) installed.

### 1. Clone the Repository

```bash
git clone [https://github.com/RoddyCodes/RPmodule8_is601.git](https://github.com/RoddyCodes/RPmodule8_is601.git)
cd RPmodule8_is601

```

### 2. Run the Application with Docker Compose

This command will build the Docker image (if it's not already built or has changed) and start the application.

```bash
docker compose up --build
```

### 3. Access the Application

Once Docker Compose indicates the application is running (you'll see Uvicorn logs), open your web browser and navigate to:

```bash
http://localhost:8000
```

### 4. Stopping the Application

To stop running Docker containers:

```bash
docker compose down
```
