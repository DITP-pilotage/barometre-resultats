import subprocess
import os
from datetime import datetime

def run_command(cmd_to_run):
    subprocess.run(cmd_to_run.split(' '))
    return

GIT_REPO_URL="github.com/DITP-pilotage/barometre-resultats.git"
GIT_BOT_USERNAME="bot-data"
GIT_BOT_EMAIL="bot-data@ditp.fr"
GIT_COMMIT_MSG="data::"+datetime.now().strftime("%d-%m-%Y")

# Credentials for pushing
GIT_USER=os.environ.get('GIT_USER')
GIT_TOKEN=os.environ.get('GIT_TOKEN')

def git_add_commit_push():
    run_command('git add ../../data/')
    run_command('git add ../../metadata/')
    # Commit avec un auteur spécifique: GIT_BOT_USERNAME
    run_command(f"git -c user.name={GIT_BOT_USERNAME} -c user.email={GIT_BOT_EMAIL} commit -m {GIT_COMMIT_MSG}")
    run_command(f'git push https://{GIT_USER}:{GIT_TOKEN}@{GIT_REPO_URL}')

if __name__ == "__main__":
    git_add_commit_push()