import subprocess
import os

def run_command(cmd_to_run):
    subprocess.run(cmd_to_run.split(' '))
    return

GIT_REPO_URL="github.com/DITP-pilotage/barometre-resultats.git"
GIT_BOT_USERNAME="bot-data"
GIT_BOT_EMAIL="bot-data@ditp.fr"
GIT_COMMIT_MSG="data::test-date"

# Credentials for pushing
GIT_USER=os.environ.get('GIT_USER')
GIT_TOKEN=os.environ.get('GIT_TOKEN')


run_command('git add ../../data/')
# Commit avec un auteur spécifique: GIT_BOT_USERNAME
run_command(f"git -c user.name={GIT_BOT_USERNAME} -c user.email={GIT_BOT_EMAIL} commit -m {GIT_COMMIT_MSG}")
run_command('git status')
run_command(f'git push https://{GIT_USER}:{GIT_TOKEN}@{GIT_REPO_URL}')

