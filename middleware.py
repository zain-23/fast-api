from fastapi import FastAPI, Request
from fastapi.responses import Response
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request:Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(duration)
    return response
