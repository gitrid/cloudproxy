import os
from loguru import logger
from cloudproxy.providers import settings


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def set_auth(username, password):
    with open(os.path.join(__location__, "user_data.sh")) as file:
        filedata = file.read()
        if settings.config["no_auth"]:
            filedata = filedata.replace("sudo sed -i 's/#BasicAuth user pass.*/BasicAuth username password/g' /etc/tinyproxy/tinyproxy.conf\n", "")
        else:
            filedata = filedata.replace("username", username)
            filedata = filedata.replace("password", password)
    logger.info(filedata)
    return filedata
