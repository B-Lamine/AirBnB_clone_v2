#!/usr/bin/python3
""" Fabfile for web site resources compression.
"""


import datetime
from fabric.api import *
import os


env.hosts = ['100.26.57.12', '100.24.242.223']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


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


def do_deploy(archive_path):
    """ Deploy archive to web servers.
    """
    if os.path.isfile(archive_path) is False:
        return False
    upload = put(archive_path, "/tmp/")
    if upload.failed is True:
        return False
    filename = archive_path.split("/")[-1]
    foldername = filename.split('.')[0]
    make_folder = run("mkdir -p /data/web_static/releases/{}"
                      .format(foldername))
    if make_folder.failed is True:
        return False
    uncompress = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
                     .format(filename, foldername))
    if uncompress.failed is True:
        return False
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}".format(foldername, foldername))
    run("rm -rf /data/web_static/releases/{}/web_static".format(foldername))
    delete_archive = run("rm /tmp/{}".format(filename))
    if delete_archive.failed is True:
        return False
    run("rm -rf /data/web_static/current")
    create_symlink = run("ln -s /data/web_static/releases/{} "
                         "/data/web_static/current".format(foldername))
    if create_symlink.failed is True:
        return False
    return True
