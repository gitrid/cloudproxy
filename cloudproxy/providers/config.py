import os
from loguru import logger
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

    logger.info(filedata)
    return filedata
