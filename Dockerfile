FROM perfsonar/testpoint:systemd
FROM python:3.9

ENV container docker

# put our code in /app in the container
COPY . /app

RUN python3 -m venv /venv
RUN . /venv/bin/activate
RUN pip install -r /app/requirements.txt

# shared volume (?)
#VOLUME /sys/fs/cgroup

# our application runs on port 80
EXPOSE 80

# Keep docker container running
CMD ["fastapi", "run", "app/pscompose/api.py", "--port", "80"]
