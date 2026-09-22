#!/bin/bash
pkill -f "python3 app.py" || true
sleep 1
cd /home/ec2-user/flask-app
nohup python3 app.py > /home/ec2-user/flask-app/app.log 2>&1 < /dev/null &
exit 0
