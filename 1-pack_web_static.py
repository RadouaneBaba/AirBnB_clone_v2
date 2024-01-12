#!/usr/bin/python3
""" archive web_static Airbnb """
from fabric.api import local
from datetime import datetime

def do_pack():
    """ generate archive and store it in versions dir """
    now = datetime.now()
    filename = now.strftime("versions/web_static_%Y%m%d%H%M%S.tgz")
    command = f"tar -czvf {filename} web_static"
    local("mkdir -p versions")
    try:
        local(command)
        return filename
    except Exception as e:
        return None
