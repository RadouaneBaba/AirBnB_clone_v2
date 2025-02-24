#!/usr/bin/python3
""" distribute archive on webservers """
from fabric.api import *
import os
env.hosts = ['54.146.94.206', '100.26.168.218']


def do_deploy(archive_path):
    """ deploy archive to webservers """
    if os.path.exists(archive_path) is False:
        return False
    try:
        name = archive_path.split('/')[1]
        name = name.split('.')[0]
        put(archive_path, "/tmp/")
        path_1 = "/tmp/{}.tgz".format(name)
        path_2 = "/data/web_static/releases/{}".format(name)
        run("mkdir -p {}".format(path_2))
        run("tar -xzf {} -C {}".format(path_1, path_2))
        run("rm {}".format(path_1))
        run("mv {}/web_static/* {}".format(path_2, path_2))
        run("rm -rf {}/web_static".format(path_2))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_2))
        print("New version deployed!")
        return True
    except Exception:
        return False
