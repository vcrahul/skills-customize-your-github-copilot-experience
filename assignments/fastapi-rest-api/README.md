# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework and Pydantic models. You'll implement CRUD endpoints, input validation, and learn how to run the app with Uvicorn.

## 📝 Tasks

### 🛠️ Implement a basic CRUD API

#### Description
Write a FastAPI application that provides create/read/update/delete operations for a simple `Item` resource using an in-memory store.

#### Requirements
Completed program should:

- Provide these endpoints:
  - `GET /items` — list all items (200)
  - `POST /items` — create a new item (201) with a validated JSON payload
  - `GET /items/{item_id}` — fetch a single item (200) or return 404 if not found
  - `PUT /items/{item_id}` — update an existing item (200) or return 404
  - `DELETE /items/{item_id}` — delete an item (204) or return 404
- Use Pydantic models for request and response validation (e.g., `name` non-empty, `price` >= 0).
- Return appropriate HTTP status codes and JSON responses.
- Track and display guessed/used IDs via the response payloads.
- Include run instructions in this README.

#### Example requests

Create an item:

```bash
curl -sS -X POST http://127.0.0.1:8000/items \
  -H 'Content-Type: application/json' \
  -d '{"name":"Apple","price":1.2}'
```

Response (201):

```json
{
  "id": "<uuid>",
  "name": "Apple",
  "description": null,
  "price": 1.2
}
```

Fetch list:

```bash
curl -sS http://127.0.0.1:8000/items
```

### 🛠️ Optional: Enhancements (bonus)

#### Description
Add one or more optional features to improve the API or developer experience.

#### Requirements
Completed program may include any of:

- Load words (data) from an external file or simple SQLite persistence.
- Add pagination or filtering to the list endpoint.
- Allow whole-object replacement and partial updates (PATCH).
- Add basic API key authentication for write endpoints.
- Provide API documentation notes or example tests using `requests`/`httpx`.

## Run instructions

1. Install dependencies:

```bash
pip install -r assignments/fastapi-rest-api/requirements.txt
```

2. Run the starter app:

```bash
python assignments/fastapi-rest-api/starter-code.py
```

Open interactive docs at: `http://127.0.0.1:8000/docs`
