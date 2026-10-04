# GitHub User Lookup

A Python command-line tool that retrieves and displays public GitHub profile data through the GitHub API.

## Features

- Looks up a GitHub account by username
- Retrieves public profile information from the GitHub API
- Displays repository count, follower count, username, and bio
- Handles profiles without a bio
- Checks HTTP response status before processing returned data

## Tech

- Python
- `requests`
- REST APIs
- JSON

## Setup

Install the required dependency:

```bash
python -m pip install requests
```

Run the program:

```bash
python github_user_lookup.py
```

## What this project demonstrates

- Making HTTP GET requests
- Working with JSON responses
- Reading structured API data
- Basic error handling
- Building URLs and processing user input
