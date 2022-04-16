#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py)
 that distributes an archive
 to your web servers, using the function do_deploy
"""

from fabric.api import *
import os.path
from os import path

env.hosts = ['34.139.139.90', '44.197.232.50']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploying the tgz file of the web_static directory"""
    if path.isfile(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        arch = archive_path.split('/')[-1]
        new_arch = archive_path.split('/')[-1].split('.')[0]
        dest = "/data/web_static/releases/"
        run('mkdir -p {}{}/'.format(dest, new_arch))
        run('tar -xzf /tmp/{} -C {}{}/'.format(arch, dest, new_arch))
        run('rm /tmp/{}'.format(arch))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(dest, new_arch))
        run('rm -rf {}{}/web_static'.format(dest, new_arch))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(dest, new_arch))
        return True
    except err:
        return False
