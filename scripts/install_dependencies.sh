#!/bin/bash
set -e
yum install -y python3 python3-pip
pip3 install -r /opt/flask-app/requirements.txt
