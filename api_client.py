import requests

def fetch_and_display_users(num_users):
    
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Make a GET request to the API
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # to check the status of HTTP

        try:
            users = response.json()  # Parse the JSON response
        except ValueError:
            print("Error: Failed to parse JSON response.")
            return None

        if not isinstance(users, list):
            print("Error: Unexpected JSON structure. Expected a list of users.")
            return None

        # Ensure we don't go out-of-bounds
        num_users_to_display = min(num_users, len(users))

        for i in range(num_users_to_display):
            user = users[i]
            try:
                name = user['name']
                email = user['email']
                city = user['address']['city']
            except KeyError as e:
                print(f"Error: Missing expected key {e} in user data.")
                continue  # Skip this user if a key is missing

            print(f"Name: {name}, Email: {email}, City: {city}")

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None

if __name__ == "__main__":
    print("Fetching 3 users:")
    fetch_and_display_users(3)

    print("\nFetching 15 users (testing out-of-bounds):")
    fetch_and_display_users(15)
