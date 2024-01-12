#!/usr/bin/python3
""" distribute archive on webservers """
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['54.146.94.206', '100.25.202.71']


def do_pack():
    """ generate archive and store it in versions dir """
    now = datetime.now()
    filename = now.strftime("versions/web_static_%Y%m%d%H%M%S.tgz")
    command = f"tar -czvf {filename} web_static"
    local("mkdir -p versions")
    try:
        local(command)
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """ deploy archive """
    if not os.path.exists(archive_path):
        return False

    name = archive_path.split('/')[1]
    name = name.split('.')[0]
    try:
        put(archive_path, "/tmp/")

        path_1 = f"/tmp/{name}.tgz"
        path_2 = f"/data/web_static/releases/{name}"

        run(f"mkdir -p {path_2}")
        run(f"tar -xzf {path_1} -C {path_2}")
        run(f"rm {path_1}")
        run(f"mv {path_2}/web_static/* {path_2}")
        run(f"rm -rf {path_2}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {path_2} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
