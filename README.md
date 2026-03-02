# Flask on Docker ![Build](https://github.com/BaralSubigya/flask-on-docker/actions/workflows/main.yml/badge.svg)

A containerized Flask backend demonstrating a simple production-style service using Docker Compose.
The application allows a user to upload an image and immediately retrieve it through a public URL.

---

## Overview

This project simulates a minimal real-world backend system. A Flask API runs inside Docker alongside a PostgreSQL container, and uploaded images are stored in a persistent volume and served back to the user.

The goal of this repository is to demonstrate:

• Multi-container architecture
• File uploads and static file serving
• Persistent storage using Docker volumes
• Clean separation of development configuration
• Automatic CI builds via GitHub Actions

After starting the containers, a user can upload an image through the browser and view it using a generated link.

---

## How to Run

Clone the repository:

```
git clone https://github.com/BaralSubigya/flask-on-docker.git
cd flask-on-docker
```

Start the application:

```
docker compose up -d --build
```

Wait about 5–10 seconds for containers to initialize.

---

## Using the Web App

### 1) Check the server

Open in browser:

```
http://localhost:8123
```

You should see:

```
{"hello":"world"}
```

---

### 2) Upload an image

Go to:

```
http://localhost:8123/upload (replace the number with the number that is unique to your port) 
```

Steps:

1. Choose any image file
2. Click **Upload**
3. A success page appears
4. Click the generated link

---

### 3) View the uploaded image

After uploading, the page provides a link like:

```
http://localhost:8123/media/yourimage.jpg (replace the number with the number that is unique to your port)
```

Opening this URL displays the uploaded image directly from the server.

---

## Key Endpoints

| Route               | Purpose               |
| ------------------- | --------------------- |
| `/`                 | Health check JSON     |
| `/upload`           | Upload form           |
| `/media/<filename>` | Serves uploaded image |

---

## Important Commands Only

Start containers:

```
docker compose up -d --build
```

Stop containers:

```
docker compose down
```

Rebuild after code changes:

```
docker compose up -d --build
```

---

## Demo

The animation below shows:

1. Starting the containers
2. Uploading an image
3. Viewing the uploaded file

![Demo](demo.gif)

---

## Author

Subigya Baral

