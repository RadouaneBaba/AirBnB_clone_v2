#!/usr/bin/python3
""" creates and distributes an archive to web servers """
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['54.146.94.206', '100.26.168.218']


def do_pack():
    """ generate archive and store it in versions dir """
    now = datetime.now()
    filename = now.strftime("versions/web_static_%Y%m%d%H%M%S.tgz")
    command = "tar -czvf {} web_static".format(filename)
    local("mkdir -p versions")
    try:
        local(command)
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """ deploy archive to webservers """
    if not os.path.exists(archive_path):
        return False

    name = archive_path.split('/')[1]
    name = name.split('.')[0]
    try:
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


def deploy():
    """ create archive and distribute it to web servers """
    archive_path = do_pack()
    return do_deploy(archive_path)
