# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI, learn how to define routes, validate request data, and return structured JSON responses while following API design best practices.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description

Create a FastAPI app that runs locally and exposes a basic health check endpoint.

#### Requirements

The completed application must:

- Import and initialize a FastAPI app instance.
- Define a root or health endpoint that returns a JSON response.
- Run the app locally with Uvicorn or the FastAPI development server.
- Confirm that the root endpoint responds successfully in the browser or with curl.

### 🛠️ Build CRUD endpoints for a resource

#### Description

Implement a simple resource such as books, tasks, or students and provide endpoints for creating, reading, updating, and deleting items.

#### Requirements

The completed API must:

- Use HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
- Store data in memory for the exercise (for example, a Python list or dictionary).
- Support creating a new resource with a JSON request body.
- Support retrieving all resources and a single resource by ID.
- Support updating an existing resource.
- Support deleting a resource.

### 🛠️ Add validation and response models

#### Description

Use FastAPI models to validate incoming data and return consistent JSON responses.

#### Requirements

The completed API must:

- Define a Pydantic model for the resource data.
- Validate required fields and enforce sensible constraints (for example, non-empty names, positive IDs, or valid status values).
- Return structured response models for resource creation and retrieval.
- Handle invalid input gracefully with proper HTTP status codes.

### 🛠️ Document and test the API

#### Description

Use FastAPI's built-in documentation and a few sample requests to confirm the API behaves correctly.

#### Requirements

The completed API must:

- Expose the interactive documentation at `/docs`.
- Use the OpenAPI-generated docs to verify each endpoint and request schema.
- Test at least one success case and one error case with sample JSON payloads.
- Include a short summary explaining how the API is organized and how each route works.
