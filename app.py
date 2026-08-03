import requests

# 1. Define the public API endpoint (returns sample JSON data)
url = "https://typicode.com"

try:
    # 2. Send the HTTP GET request
    response = requests.get(url, timeout=5)
    
    # 3. Raise an exception if the request failed (e.g., 404, 500)
    response.raise_for_status()
    
    # 4. Parse the response body as JSON
    data = response.json()
    
    # 5. Print the retrieved data
    print("✅ Data fetched successfully!")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")

except requests.exceptions.HTTPError as http_err:
    print(f"❌ HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("❌ Error: Could not connect to the server.")
except requests.exceptions.Timeout:
    print("❌ Error: The request timed out.")
except requests.exceptions.RequestException as err:
    print(f"❌ An error occurred: {err}")
