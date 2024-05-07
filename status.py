import requests

# Function to send HTTP request to API and handle response
def send_api_request(method, url, data=None):
    global response
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url)

        status_code = response.status_code
        response_content = response.json() if response.text else None  # Parse JSON if response content is not empty

        return status_code, response_content

    except requests.exceptions.RequestException as e:
        return None, f"Error: {e}"

# Main function
def main():
    # API endpoint base URL
    base_url = "https://reqres.in/api/users"

    # User input for API endpoint, method, and data
    endpoint = input("Enter API endpoint (e.g., '/employees/{id}', '/create'): ")
    method = input("Enter HTTP method (GET, POST, PUT, DELETE): ").upper()

    #User id
    user_id = input("Enter user ID (if applicable): ")
    # Construct API URL
    if endpoint.capitalize() != "None":
        url = base_url + endpoint.format(id=user_id)
    else:
        url = base_url

    # Append user ID to the URL if provided
    if user_id.capitalize() != "None":
        url += f"/{user_id}"

    # Send API request and handle response
    status_code, response_content = send_api_request(method, url)

    # Print status code and response content
    print(f"API {method} {url} returned status code: {status_code}")
    if response_content is not None:
        print("Response content:", response_content)
    else:
        print("Response content is empty.")
    # Generate report
    report = f"""
    API Request Details:
    - URL: {url}
    - Method: {method}
    - User ID: {user_id}
    
    API Response Details:
    - Status Code: {status_code}
    """
    if response_content is not None:
        report += f"- Response Content: {response_content}"

    print(report)
if __name__ == "__main__":
    main()
