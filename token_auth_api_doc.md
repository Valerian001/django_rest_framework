
# 📘 API Documentation: Token Authentication with Django REST Framework

This API uses **Token-based Authentication**. Clients must first obtain an authentication token using their credentials, then include that token in the `Authorization` header of subsequent requests.

---

## 🔐 Authentication Flow

1. Send username and password to the `/api/token/` endpoint.
2. Receive an authentication token.
3. Include the token in the `Authorization` header as:
   ```
   Authorization: Token your_token_here
   ```
4. Access protected endpoints.

---

## 🔑 Obtain Authentication Token

**Endpoint:**

```
POST /api/token/
```

**Description:**

Returns a token for a user given valid credentials.

**Request Headers:**

```
Content-Type: application/json
```

**Request Body:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Success Response:**

```json
{
  "token": "abc123yourauthtoken"
}
```

**Error Response (Invalid credentials):**

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

**Example cURL:**

```bash
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "adminpass"}'
```

---

## ✅ Protected Endpoint: HelloView

**Endpoint:**

```
GET /api/hello/
```

**Description:**

Returns a greeting to authenticated users.

**Request Headers:**

```
Authorization: Token your_token_here
```

**Success Response:**

```json
{
  "message": "Hello, admin!"
}
```

**Error Response (Unauthorized):**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

**Example cURL:**

```bash
curl -X GET http://localhost:8000/api/hello/ \
-H "Authorization: Token abc123yourauthtoken"
```

---

## 📁 API Endpoint Summary

| Method | Endpoint        | Authentication | Description                         |
|--------|-----------------|----------------|-------------------------------------|
| POST   | /api/token/     | ❌              | Obtain auth token using credentials |
| GET    | /api/hello/     | ✅              | Return greeting for logged-in user  |

---

## 🧪 Testing Notes

- Use Postman or `curl` to obtain and test tokens.
- Always include the token in the `Authorization` header.
- Token must be sent with the `Token` prefix:
  ```
  Authorization: Token your_token_here
  ```
