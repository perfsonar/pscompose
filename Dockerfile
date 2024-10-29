FROM perfsonar/testpoint:systemd
FROM python:3.9

ENV container docker

# put our code in /app in the container
COPY . /app

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
CMD ["fastapi", "run", "app/pscompose/api/api.py", "--port", "80"]
