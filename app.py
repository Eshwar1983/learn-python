import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your React app's Render URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("testdb")


@app.get("/api/data")
async def get_data():
  items = await db.items.find().to_list(100)
  for item in items:
    item["_id"] = str(item["_id"])
  return {"message": "Hello from Python!", "items": items}
