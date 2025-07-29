import os
from ali_backend.routes import ping
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from ali_backend.routes import db_test

app = FastAPI()
app.include_router(ping.router)
app.include_router(db_test.router)
static_file_path = os.path.dirname(os.path.realpath(__file__)) + "/static"
app.mount("/static", StaticFiles(directory=static_file_path), name="static")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")
