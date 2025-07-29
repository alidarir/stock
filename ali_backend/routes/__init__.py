from fastapi import FastAPI
from ali_backend.routes import ping

app = FastAPI()
app.include_router(ping.router)
