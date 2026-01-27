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
    - Enforces an access control check: If the request does not include 
      the header "Access-X-Control: True", it redirects to Bing instead.

Use Case:
    - This function can be deployed in AWS Lambda behind an API Gateway, allowing it to serve
      as an intermediary redirector for red team engagements or adversarial simulation exercises.

=========================================================================================
"""

import base64
import json
import requests

# Define the target URL and the fallback redirect URL
TARGET_URL = "https://stigscorp.org"
FALLBACK_URL = "https://www.bing.com"

def lambda_handler(event, context):
    """
    AWS Lambda function to handle request redirection with security enforcement.
    """

    # Extract HTTP method, path, and query string
    method = event["requestContext"]["http"]["method"]
    path = event["requestContext"]["http"]["path"]
    query_string = event.get("rawQueryString", "")

    # Extract headers (convert to lowercase for case-insensitive lookup)
    inbound_headers = {k.lower(): v for k, v in event.get("headers", {}).items()}

    # Validate the required HTTP header (case-insensitive check)
    if inbound_headers.get("access-x-control") != "True":
        return {
            "statusCode": 302,
            "headers": {"Location": FALLBACK_URL},  # Silent redirect
        }

    # Construct full target URL
    url = f"{TARGET_URL}{path}"
    if query_string:
        url += f"?{query_string}"

    # Handle request body (decode if base64 encoded)
    body = event.get("body", "")
    if event.get("isBase64Encoded", False):
        body = base64.b64decode(body)

    # Forward request dynamically
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=inbound_headers,
            data=body,
            verify=False  # SSL verification disabled for self-signed certificates
        )

        return {
            "statusCode": response.status_code,
            "headers": dict(response.headers),
            "body": response.text,
            "isBase64Encoded": False
        }

    except:
        return {
            "statusCode": 302,
            "headers": {"Location": FALLBACK_URL},  # Silent redirect on failure
        }