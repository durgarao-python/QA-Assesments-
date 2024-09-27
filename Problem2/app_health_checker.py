import requests

# URL of the application to check
APPLICATION_URL = "http://example.com"  # Replace with your application's URL

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Application is UP.")
        else:
            print(f"Application is DOWN: Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking application: {e}")

if __name__ == "__main__":
    check_application_health(APPLICATION_URL)
