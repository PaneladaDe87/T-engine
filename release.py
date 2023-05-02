import requests

api_url = "https://github.com/PaneladaDe87/T-engine"
response = requests.get(api_url)

if response.status_code == 200:
    latest_release = response.json()["tag_name"]
    print(f"Latest release: {latest_release}")
else:
    print("Failed to get latest release information.")
