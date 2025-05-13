import requests

def login(username: str, password: str) -> dict:
    try:
        response = requests.post('http://localhost:5001/login', json={'email': username, 'password': password})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def register(username: str, password: str, name: str) -> dict:
    try:
        response = requests.post('http://localhost:5001/register', json={'email': username, 'password': password, 'name': name})
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {"success": False, "message": str(e)}