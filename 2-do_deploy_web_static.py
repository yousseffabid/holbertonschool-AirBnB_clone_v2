#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from fabric.api import local, put, run, env
import os.path


env.hosts = ['54.87.26.7', '34.227.226.141']


def do_deploy(archive_path):
    """distributes an archive to web servers"""

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if os.path.isdir(archive_path) is False:
        return False

    if put(archive_path, "/temp/{}".format(file)).failed is True:
        return False

    if run("tar -zxf /tmp/{} -C /data/web_static/releases/{}".format
           (file, name)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False

    if run("rm -rf /temp/{}".format(file)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False

    return True
