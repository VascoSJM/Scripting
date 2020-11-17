import os
import time
from pathlib import Path
from secrets import token_hex
from github import Github
from github import NamedUser

# Get repo path
path_prefix = str(Path.home().joinpath('Projects'))  # Projects folder
user_input = ""
while True:
    user_input = input("FOLDER REPO PRIVATE['t' or 'f']: ").split(" ")
    if len(user_input) != 3 or (user_input[2] != "t" and user_input[2] != "f"):
        print("Invalid input! Please try again.")
    else:
        break

language, repo, private = user_input
path = f"{path_prefix}/{language}/{repo}"

# Create project folder and subfolders
while True:
    try:
        os.makedirs(path)
        break
    except FileExistsError as e:
        token = token_hex(3)
        path += token   # If folder exists add 6-digit string
        repo += token   # Also update the repo name for GitHub

# Get user
github_token = os.environ.get("GITHUB_TOKEN")
user = Github(github_token).get_user()

# Set the private variable p
p = True if private == "t" else False

# Create Repo
user.create_repo(repo, private=p)

# Initialize the repository
os.chdir(path)
os.system('git init')
os.system('touch README.md')
os.system('git add .')
os.system('git commit -m "Initial commit"')
os.system('git branch -M main')
os.system(f'git remote add origin https://github.com/VascoSJM/{repo}.git')
os.system('git push -u origin main')
