import os
from datetime import datetime, timedelta

def create_commit_in_past(days_ago: int, commit_message: str):
    # Calculate the date 'days_ago' days ago
    commit_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d %H:%M:%S')

    # Set the GIT_COMMITTER_DATE environment variable for the commit date
    os.environ['GIT_COMMITTER_DATE'] = commit_date

    # Stage changes for the new commit
    os.system('git add .')

    # Commit with the specified date
    os.system(f'git commit -m "{commit_message}"')

    # Unset the GIT_COMMITTER_DATE environment variable
    del os.environ['GIT_COMMITTER_DATE']

# Number of days to go back in time for the new commit
num_days_ago = 2

# Commit message for the new commit
commit_message = "This is a commit from a week ago."

# Run the function to create a new commit in the past
create_commit_in_past(num_days_ago, commit_message)