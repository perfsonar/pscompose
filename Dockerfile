FROM perfsonar/testpoint:latest

ENV container docker

RUN mkdir -p /etc/pscompose

# put our code in /app in the container
COPY . /app
COPY docker/start.sh /
COPY EXAMPLE_CONFIG.yml /etc/pscompose/settings.yml

RUN apt-get update && apt-get install -y python3.10 python3.10-venv python3-pip libpq-dev

RUN python3 -m venv /venv
RUN . /venv/bin/activate
RUN pip install -r /app/requirements.txt

# TODO: 
# - Ensure postgres is running
# - The image needs a pScheduler instance running
# - Put the SQL in place to initialize the storage tables
# - write all of the python code for the API
# - wrap the pScheduler API return stuff for the pSCompose UI
# - code the UI
# - profit

# our application runs on port 80
EXPOSE 80

# Keep docker container running
CMD ["/bin/sh", "/start.sh"]
