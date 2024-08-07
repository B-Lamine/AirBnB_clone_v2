#!/usr/bin/python3
""" Fabfile for web site resources compression.
"""


import datetime
from fabric.api import *


def do_pack():
    """ Local compression command.
    """
    update_date = datetime.datetime.now()
    filename = "web_static_{}.tgz".format(update_date.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    with lcd("versions"):
        test = local("tar -cvzf {} ../web_static".format(filename))
        if test.succeeded is True:
            filepath = local("realpath {}".format(filename), capture=True)
            return filepath
        else:
            return None
