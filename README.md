![CI](https://github.com/BaralSubigya/flask-on-docker/actions/workflows/main.yml/badge.svg)

# flask-on-docker

## Overview

This repository contains a fully containerized Flask web application built using a multi-service architecture inspired by the Instagram-style backend stack. The project uses Docker Compose to orchestrate multiple services, including a Flask web server, a PostgreSQL database, and supporting infrastructure within isolated containers. The application allows users to upload image files and retrieve them through a served media endpoint, demonstrating file handling, persistent storage, and HTTP routing in a web service environment. The purpose of this project is to showcase practical experience with containerized development workflows, service communication, and reproducible deployment setups, ensuring that the application can be built and run consistently across different machines using only Docker.

## Demo
(Add demo.gif after recording)

![demo](demo.gif)

## Build / Run Instructions

Start:
docker compose up -d --build

Open in browser:
http://localhost:8123

Upload example:
curl -F "file=@/path/to/image.jpg" http://localhost:8123/upload

Then open returned URL:
http://localhost:8123/media/image.jpg

## Security
Production credentials are excluded using .gitignore.
