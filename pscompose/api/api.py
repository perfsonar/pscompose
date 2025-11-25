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
app = FastAPI()

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
