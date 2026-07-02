import urllib.request
import json

url = 'http://127.0.0.1:5000/api/courses/'
data = {
    "name": "Introduction to Python",
    "code": "PY101",
    "credits": 3,
    "department_id": 1
}

# Convert the Python dictionary to a JSON string, then encode it to bytes
json_data = json.dumps(data).encode('utf-8')

# Create the request, telling the server we are sending JSON
req = urllib.request.Request(url, data=json_data, headers={'Content-Type': 'application/json'})

try:
    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print("Success! The API returned:")
        print(json.dumps(result, indent=2))
except Exception as e:
    print(f"An error occurred: {e}")