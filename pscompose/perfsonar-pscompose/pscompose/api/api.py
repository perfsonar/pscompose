import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pscompose.api.routers import (
    addresses,
    archives,
    basic_auth,
    contexts,
    groups,
    schedules,
    tasks,
    templates,
    tests,
    home,
)

# initialize FastAPI application
# root_path tells FastAPI the proxy prefix so that redirects (e.g. trailing-slash
# 307s) and generated URLs include the full path rather than a bare root-relative one.
# The value is read from the SCRIPT_NAME env var set in the systemd unit file;
# it falls back to '' so dev environments work unchanged.
app = FastAPI(root_path=os.environ.get("SCRIPT_NAME", ""))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5001", "http://127.0.0.1:5001"],  # your frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include submodule routers
for lib in [addresses, archives, basic_auth, contexts, groups, schedules, tasks, templates, tests, home]:
    app.include_router(lib.router)


# include our hello_world route
@app.get("/")
async def root():
    return {"message": "Hello World"}
