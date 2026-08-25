# GitHub User Lookup

A beginner Python project that retrieves public profile information from the GitHub API.

## Features

- Prompts for a GitHub username
- Retrieves public profile information using the GitHub API
- Displays the username, public repository count, follower count, and bio
- Handles accounts that do not have a bio

## Requirements

- Python 3
- The `requests` library

Install the dependency with:

```bash
python -m pip install requests
```

## Usage

Run the program:

```bash
python github_user_lookup.py
```

Enter a GitHub username when prompted.

## What I Learned

- Making HTTP GET requests with `requests`
- Working with JSON responses
- Reading values from Python dictionaries
- Checking HTTP status codes
- Building URLs with f-strings
