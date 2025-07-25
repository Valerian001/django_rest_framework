# 📘 API Documentation: Custom Token Authentication with Phone Number and OTP (Django REST Framework)

## 🔐 Overview

This API uses Token Authentication for secure access. Users register with their phone number and name. OTP is sent using EbulkSMS for phone verification. Once verified, users receive an authentication token for future requests.

---

## 📥 1. Register User

**POST** `/api/register/`

Send user data to initiate registration and trigger OTP sending to the phone.

### Request Body
```json
{
  "name": "John Doe",
  "phone_number": "2348012345678",
  "password": "securepass123"
}
```

### Response
```json
{
  "message": "OTP sent to phone."
}
```

---

## ✅ 2. Verify Phone Number

**POST** `/api/verify-phone/`

Verify the OTP sent to the user's phone and return a token.

### Request Body
```json
{
  "phone_number": "2348012345678",
  "otp": "1234"
}
```

### Response
```json
{
  "token": "abc123tokenkey"
}
```

### Error Response
```json
{
  "error": "Invalid OTP"
}
```

---

## 🔑 3. Login

**POST** `/api/login/`

Authenticate using `phone_number` and `password` to receive a token.

### Request Body
```json
{
  "phone_number": "2348012345678",
  "password": "securepass123"
}
```

### Response
```json
{
  "token": "abc123tokenkey"
}
```

---

## 🔒 4. List Users

**GET** `/api/users/`

Returns a list of all registered users. Requires token authentication.

### Headers
```
Authorization: Token abc123tokenkey
```

### Response
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "phone_number": "2348012345678"
  },
  ...
]
```

---

## 🌐 Summary of Endpoints

| Endpoint              | Method | Auth Required | Description                  |
|-----------------------|--------|----------------|------------------------------|
| `/api/register/`      | POST   | ❌             | Initiate registration & OTP  |
| `/api/verify-phone/`  | POST   | ❌             | Verify OTP & get token       |
| `/api/login/`         | POST   | ❌             | Login and get token          |
| `/api/users/`         | GET    | ✅             | List users (protected)       |

---

## 📩 SMS Gateway

EbulkSMS API is used to send OTPs to users during registration. Ensure API credentials are correctly configured in `utils/sms.py`.
