#!/usr/bin/python3
""" archive web_static Airbnb """
from fabric.api import local
from datetime import datetime


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
