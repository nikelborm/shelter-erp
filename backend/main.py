from fastapi import FastAPI
import asyncio
from src import api_router
from src.db.migrate import migrate, mock
import os


if os.environ.get('MODE') == 'migration':
  asyncio.run(migrate())
  exit()

if os.environ.get('MODE') == 'mock':
  asyncio.run(mock())
  exit()

app = FastAPI()

app.include_router(api_router.api_router)
