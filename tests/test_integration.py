import requests

# URL of the frontend service
FRONTEND_URL = "http://localhost:30000"  # Update based on your service

def test_frontend():
    try:
        response = requests.get(FRONTEND_URL)
        if response.status_code == 200:
            if "Hello, World!" in response.text:  # Expected greeting message
                print("Test Passed: Greeting message is displayed correctly.")
            else:
                print("Test Failed: Greeting message not found.")
        else:
            print(f"Test Failed: Frontend returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

if __name__ == "__main__":
    test_frontend()
