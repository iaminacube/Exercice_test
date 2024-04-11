import requests

# Function to fetch data from API
def fetch_data_from_api():
    url = 'https://www.common.com/cmn-api/listings/common'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data from API:", response.status_code)
        return None

# Main function
def main():
    # Fetch data from API
    api_data = fetch_data_from_api()
    if api_data:
        # Process the retrieved data
        for item in api_data:
            print(item)
    else:
        print("Failed to fetch data from API.")

if __name__ == "__main__":
    main()
