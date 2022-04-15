#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """"creating a .tgz archive of the AirBnB web_static folder
        with a timestamp
    """
    date = datetime.now()
    timestamp = date.strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    tgzFile = "versions/web_static_{}.tgz".format(timestamp)
    tar = local("tar -cvzf {} web_static".format(tgzFile))

    if tar.failed:
        return None
    return tgzFile
