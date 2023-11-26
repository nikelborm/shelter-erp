import os
import asyncio
from src.db.migrate import migrate, mock
if os.environ.get('MODE') == 'migration':
  asyncio.run(migrate())
  exit()

if os.environ.get('MODE') == 'mock':
  asyncio.run(mock())
  exit()

# These chapters separate to allow migrations even if all other code is broken

from fastapi import FastAPI
from src import api_router
app = FastAPI()

app.include_router(api_router)
