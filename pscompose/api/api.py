from fastapi import FastAPI, Request
from fastapi_versioning import version

from pscompose.api.routers import basic_auth, templates, hosts, tests

# initialize FastAPI application
app = FastAPI()

# include submodule routers
for lib in [basic_auth, templates, hosts, tests]:
    app.include_router(lib.router)

# include our hello_world route
@app.get("/")
async def root():
    return {"message": "Hello World"}
