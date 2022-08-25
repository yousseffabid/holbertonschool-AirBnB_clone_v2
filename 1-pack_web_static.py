#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from fabric.api import local
import os.path
from datetime import datetime


def do_pack():
    """archive webs_static folder"""
    d = datetime.utcnow()
    web_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(d.year,
                                                             d.month,
                                                             d.day,
                                                             d.hour,
                                                             d.minute,
                                                             d.second)

    if local("mkdir -p versions").failed is True:
        return None
    if local("tar -cvzf {} web_static".format(web_file)).failed is True:
        return None
    return web_file
