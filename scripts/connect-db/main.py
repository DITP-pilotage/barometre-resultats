from sshtunnel import SSHTunnelForwarder
import utils
import os
from dotenv import load_dotenv


# [config]
load_dotenv()

## [ssh-tunnel]
SSH_LOCAL_PORT = 10010
SSH_LOCAL_ADDR = "127.0.0.1"

## [db-url]
PG_URL="".join([
    "postgresql+psycopg2://",
    os.environ.get("PG_USER", "none"),
    ":",
    os.environ.get("PG_PWD", "none"),
    "@",SSH_LOCAL_ADDR,":",str(SSH_LOCAL_PORT),"/",
    os.environ.get("PG_DATABASE", "none"),
])


# Connect to Scalingo instance via SSH tunnel
with SSHTunnelForwarder(
    (os.environ.get("SCALINGO_SSH_HOST", "none"), 22),
    ssh_username="git",
    ssh_private_key=os.environ.get("SCALINGO_PATH_TO_PRIVATEKEY", "none"),
    remote_bind_address=(os.environ.get("SCALINGO_REMOTE_HOST", "none"), int(os.environ.get("SCALINGO_SSH_PORT", 00))),
    local_bind_address=(SSH_LOCAL_ADDR, SSH_LOCAL_PORT)
) as tunnel:
    print("SSH tunnel established")


    # Récupération des données du baro
    donnees_baro = utils.get_data("Base cible", PG_URL)

    print(donnees_baro)