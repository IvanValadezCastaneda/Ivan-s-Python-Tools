import git

# Path to the Git executable
git_path = r'C:\Program Files\Git\bin\git.exe'

# List of directories to update
dirs_to_update = [
    #r'C:\path\to\first\directory',
    #r'C:\path\to\second\directory'
    r'C:\SimpleNodeJsBackend\SimpleNodeJsBackend'
]

# Loop through each directory and update it
for dir in dirs_to_update:
    # Open the Git repository
    repo = git.Repo(dir)

    # Pull changes from the remote repository
    origin = repo.remote(name='origin')
    origin.pull(rebase=True)
