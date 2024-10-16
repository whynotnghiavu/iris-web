import os
import time
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.users.routers.users import user_router

# Set the timezone to Asia/Ho_Chi_Minh
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
time.tzset()

# Config file logger
log_file_format = "{time:YYYY-MM-DD}.log"
logger.add(f"logger/{log_file_format}", rotation="00:00", retention="7 days", enqueue=True)


# Get the `SERVER_IP` from the `.env` file
load_dotenv()
server_ip = os.getenv("SERVER_IP", "localhost")
environment = os.getenv("ENVIRONMENT", "PRODUCTION")


app = FastAPI()


# Allow all origins, methods and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)


@app.get("/")
def root():
    return {'message': 'Hello World'}


if __name__ == "__main__":
    uvicorn.run(app, host=server_ip, port=8009)
