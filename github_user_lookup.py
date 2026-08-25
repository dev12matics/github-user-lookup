import requests


username = input("Enter a GitHub username: ")

url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()

    login = user_data.get("login")
    public_repos = user_data.get("public_repos")
    followers = user_data.get("followers")
    bio = user_data.get("bio")

    print(f"Name: {login}")
    print(f"Public Repos: {public_repos}")
    print(f"Followers: {followers}")
    print(f"Bio: {bio if bio else 'Sorry, no bio available!'}")
else:
    print("Failed to fetch data!")
