# pSCompose

A graphical interface for composing perfSONAR configurations

## General Instructions

Create a virtualenv, activate it and install packages

**Note:** You want to be on Python3.11 or above. Check this by running `python3 --version`

```
python -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## API

### Step One: Setup

Install postgresql 14
```
brew install postgresql@14
```

Now, run the following commands
```
sudo mkdir -p /etc/pscompose
cd /etc/pscompose
sudo vi settings.yml 
    --> Copy paste the EXAMPLE_CONFIG.yml
chmod +x local_setup.sh
./local_setup.sh
```

The script (local_setup.sh) will:
- Start PostgreSQL if needed
- Create the pscompose_user with password 'password'
- Create the database with pscompose_user as the owner
- Grant all necessary permissions
- Set up the Python environment
- Create the tables

Next, check if postgresql is running. If not, start it manually
```
brew services info postgresql
brew services start postgresql
```

To view the postgres database, run

```
psql -U pscompose_user pscompose
\dt
SELECT * FROM data;
\q
```

### Step Two: Run the API

To start the API locally, 

```
make run-api
```

You should then be able to point your browser to:

```
http://0.0.0.0:8000/docs
```

## (In progress, ignore for now) API & General Development

We'll be targeting a vagrant VM image. The image will have a running pScheduler instance, and will spin up a running pSCompose instance (eventually).

To get the development environment running:

**Note**: This will run the start.sh script in docker/start.sh

```
make docker
```

from the top-level directory. You should then be able to point your browser to:

```
http://localhost:8888/docs
```

Another method is to run `docker compose up --build` which will rebuild the images for the services defined in docker-compose.yml that have a build section and then start the containers using those images.

## Fronend / HTML Mockup Development

While we are working on the initial HTML mockups, there will be two steps required to run tailwindcss to watch for changes to the HTML files. These steps should be run in separate shells.

**Note:** Use node v18 or beyond

### Step One: Tailwind CSS build

You can start it with this convenient make command:

```
make css-watch
```

This will update the output CSS file in `pscompose/frontend/css/pscompose.css`. This file will need to be included in each HTML mockup using a <link> tag ('in the normal way'):

```
<link rel="stylesheet" href="../css/pscompose.css">
```

(NB: `../css/pscompose.css` is relative to the position of the mockups folder with reference to the root of the running HTTP server)

### Step Two: Start the python SimpleHTTPServer

This will start a simple HTTP Server that just serves the files under pscompose/frontend

```
make run-frontend
```

You should be able to see the frontend at: `http://localhost:5001/`
