# pscompose
A graphical interface for composing perfSONAR configurations

## API & General Development

We'll be targeting a vagrant VM image. The image will have a running pScheduler instance, and will spin up a running pSCompose instance (eventually).

To get the development environment running:

```
make docker-build
make docker
```

from the top-level directory. You should then be able to point your browser to:

```
http://localhost:8888/docs
```

Another method is to run `docker compose up --build` which will rebuild the images for the services defined in docker-compose.yml that have a build section and then start the containers using those images.

## Fronend / HTML Mockup Development

While we are working on the initial HTML mockups, there will be two steps required to run tailwindcss to watch for changes to the HTML files. These steps should be run in separate shells.

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
make run-mockups
```

You should be able to see the mockups at: `http://localhost:8000/mockups/`

