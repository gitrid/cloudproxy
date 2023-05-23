import os
from loguru import logger
import requests
from cloudproxy.providers import settings


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def set_auth(username, password):
    if settings.config["no_auth"]:
        with open(os.path.join(__location__, "user_data_no_auth.sh")) as file:
            filedata = file.read()
    else:
        with open(os.path.join(__location__, "user_data.sh")) as file:
            filedata = file.read()
            filedata = filedata.replace("username", username)
            filedata = filedata.replace("password", password)

    if settings.config["only_host_ip"]:
        ip_address = requests.get('https://ipecho.net/plain').text.strip()
        filedata = filedata.replace("ufw allow 22/tcp", f"sudo ufw allow from {ip_address} to any port 22 proto tcp")
        filedata = filedata.replace("ufw allow 8899/tcp", f"sudo ufw allow from {ip_address} to any port 8899 proto tcp")

    logger.info(filedata)
    return filedata
