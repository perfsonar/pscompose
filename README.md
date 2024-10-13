# pscompose
A graphical interface for composing perfSONAR configurations

## Development
We'll be targeting a vagrant VM image. The image will have a running pScheduler instance, and will spin up a running pSCompose instance (eventually).

To get the development environment running:

```
vagrant up
```

from the top-level directory. You should then be able to point your browser to:

```
[TBD]
```

## How to run (API demo)

```
➜  pscompose git:(api-demo) python3 -m venv venv
➜  pscompose git:(api-demo) ✗ source venv/bin/activate
(venv) ➜  pscompose git:(api-demo) ✗ pip install fastapi uvicorn
```