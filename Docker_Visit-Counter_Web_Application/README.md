# End-to-end Visit Counter Web Application
### End-to-End deployment of a page counter application using Docker Compose, Nginx, Flask, and Redis (for volume persistence).

---

## Contents

- [Core Technologies](#core-technologies)
- [Project Overview](#project-overview)
- [Demo of the Application](#demo-of-the-application)
- [How it works](#how-it-works)
- [Key Features](#key-features)
- [Future Improvements](#future-improvements)
- [Instructions to reproduce the setup](#instructions-to-reproduce-the-setup)

---

## Core Technologies
![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![](https://img.shields.io/badge/Redis-red?style=for-the-badge&logo=redis&logoColor=white)

---

### Project Overview
This project demonstrates how a simple Flask application can be containerised and connected to a Redis data store using Docker Compose. Nginx provides the entry point to the application, while Redis maintains the visitor count using persistent storage. 

---

### Demo of the Application

https://github.com/user-attachments/assets/75f9bb94-0b2f-4438-b056-bafae92c6bb3

*The recording demonstrates the application running locally,
including application information pages and Redis-backed visitor counter.*

---
### How it works

```
                  ┌──────────────┐
                  │    Browser   │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │    Nginx     │
                  │ Reverse Proxy│
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │    Flask     │
                  │ Web Service  │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │    Redis     │
                  │ Data Store   │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ Redis Volume │
                  │  Persistent  │
                  │    Data      │
                  └──────────────┘
```

- A user visits /count.
- Flask receives the request.
- Flask connects to Redis.
- Redis increments the visits key.
- Flask retrieves the resulting value.
- The count is displayed in the browser.

---

### Key features
#### Containerisation
Containerised the Flask application and supporting services using Docker and Docker Compose, creating a reproducible multi-container development environment.

#### Service Architecture
Implemented a three-service architecture using Flask, Redis and Nginx, with services communicating through an isolated Docker network.

#### Persistent Data
Configured Redis persistence using append-only files and a Docker-managed volume to retain visitor data across container restarts.

#### Reverse Proxy
Configured Nginx as a reverse proxy, providing a single-entry point to the application while keeping the Flask service isolated from direct external access.

#### Configuration
Used environment variables to decouple application configuration from the container image and support flexible deployment environments.

#### Application Design
Implemented Redis's atomic INCR operation to safely maintain the visitor count across requests.

---

### What I learnt
- How containers communicate through Docker Compose networking
- How Redis persistence works
- How reverse proxies sit in front of application services
- How environment variables can be used for container configuration
- How service dependencies affect container startup
- How to troubleshoot multi-container applications

---

### Future Improvements

#### Application
- Add a health-check endpoint such as /health
- Add a separate read endpoint for the current visitor count
- Add better error handling when Redis is unavailable
- Add automated tests for Flask routes
- Add a reset/admin endpoint protected by authentication

#### Docker
- Reduce image size using multi-stage builds
- Run the Flask container as a non-root user
- Add Docker health checks
- Pin image versions instead of using floating tags
- Improve container security scanning

#### CI/CD
- Introduce GitHub Actions to automatically build, test and scan Docker images on every push.

#### Observability
- Prometheus metrics
- Grafana dashboards
- Container health monitoring
- Centralised logging
- Redis metrics
- Application response-time monitoring


### Instructions to reproduce the setup
- clone repository
```
https://github.com/umaratimomo-hub/Docker_Learning/tree/main/Docker_Page-Count_Web_Application
```

- Enter the project folder
```
cd Docker_Page-Count_Web_Application
```

- run the containers
```
docker-compose up
```

- click link to view on local host browser port 5001
