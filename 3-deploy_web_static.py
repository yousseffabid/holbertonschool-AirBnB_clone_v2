#!/usr/bin/python3
"""creates and distributes an archive to web servers"""

import os.path
from fabric.api import put
from fabric.api import run
from fabric.api import env
from fabric.api import local
from datetime import datetime

env.hosts = ['54.87.26.7', '34.227.226.141']


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


def do_deploy(archive_path):
    """distributes an archive to web servers"""

    web_file = archive_path.split("/")[-1]
    name = web_file.split(".")[0]

    if os.path.isfile(archive_path) is False:
        return False

    if put(archive_path, "/tmp/{}".format(web_file)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(web_file, name)).failed is True:
        return False

    if run("rm /tmp/{}".format(web_file)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False

    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
