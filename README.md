# About LCL-Power-API
REST API Electricity Parameters

# API Framework and Authentication method

This API is a RESTFUL API developed by Flask and Python. The API uses HTTP Basic Authentication for securing endpoints. The username and password should be provided in the request headers.

#### Request

- **URL:** `/v1/table`
- **Method:** `POST`
- **Authentication:** Required

#### Request Body

| Parameter      | Type     | Description                           |
|----------------|----------|---------------------------------------|
| `table`        | string   | Name of the table to query            |
| `bidding_zone` | string   | Name of the bidding zone              |
| `date_from`    | string   | Start date (YYYY-MM-DD HH:MM:SS)      |
| `date_to`      | string   | End date (YYYY-MM-DD HH:MM:SS)        |

#### Response

- **Status Code:** 200 OK
- **Content-Type:** application/json

##### Successful Response Body

A JSON array containing the requested data.

##### Error Response Body

In case of errors, a JSON object with an error message will be returned.

- **Status Code:** 404 Not Found or 500 Internal Server Error
- **Content-Type:** application/json

#### Example

```http
POST /v1/table HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Authorization: Basic Base64Encoded(LCL:pw)

table=actual_generation&bidding_zone=example_zone&date_from=2023-01-01 00:00:00&date_to=2023-01-02 00:00:00
```

#### Database Structure/Relationship

