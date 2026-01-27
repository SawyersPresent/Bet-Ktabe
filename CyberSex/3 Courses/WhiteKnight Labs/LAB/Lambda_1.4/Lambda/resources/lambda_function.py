"""
=========================================================================================
ARTOC Course - White Knight Labs
Created by: Stigs

Description:
    This AWS Lambda function is designed for the Advanced Red Team Operations Certification (ARTOC) 
    course by White Knight Labs. It acts as an external redirector, forwarding all incoming 
    HTTP traffic (including headers, query parameters, and request bodies) to an external 
    HTTPS endpoint.

Key Features:
    - Supports all HTTP methods (GET, POST, PUT, DELETE, etc.).
    - Preserves query strings, headers (including User-Agent), and request bodies.
    - Handles Base64-encoded payloads when necessary.
    - Disables SSL verification for self-signed certificates.
    - Forwards responses from the external server back to the client.

Use Case:
    - This function can be deployed in AWS Lambda behind an API Gateway, allowing it to serve
      as an intermediary redirector for red team engagements or adversarial simulation exercises.

=========================================================================================
"""

import base64
import json
import requests

TARGET_URL = "https://stigscorp.org"

def lambda_handler(event, context):
    # print("===== Incoming Request =====")
    # print(json.dumps(event, indent=2))

    # Extract HTTP method, path, and query string
    method = event["requestContext"]["http"]["method"]
    path = event["requestContext"]["http"]["path"]
    query_string = event.get("rawQueryString", "")

    # Construct full target URL
    url = f"{TARGET_URL}{path}"
    if query_string:
        url += f"?{query_string}"

    # Extract headers and print User-Agent
    inbound_headers = event.get("headers", {})
    user_agent = inbound_headers.get("User-Agent", "No User-Agent Provided")
    # print(f"User-Agent: {user_agent}")

    # print("Headers:", json.dumps(inbound_headers, indent=2))

    # Handle request body
    body = event.get("body", "")
    if event.get("isBase64Encoded", False):
        body = base64.b64decode(body)
    # print(f"Request Body: {body}")

    # print(f"Forwarding request to: {url} using method {method}")

    # Forward request dynamically
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=inbound_headers,
            data=body,
            verify=False  # Disabling SSL verification
        )

        # print("===== Response from Target URL =====")
        # print(f"Status Code: {response.status_code}")
        # print("Response Headers:", json.dumps(dict(response.headers), indent=2))
        # print(f"Response Body: {response.text}")

        return {
            "statusCode": response.status_code,
            "headers": dict(response.headers),
            "body": response.text,
            "isBase64Encoded": False
        }

    except requests.exceptions.RequestException as e:
        # print(f"Error forwarding request: {e}")

        return {
            "statusCode": 502,
            "body": json.dumps({"error": "Bad Gateway", "message": str(e)})
        }