from typing import Union

from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "la"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    config = uvicorn.Config(app, port=8000)
    server = uvicorn.Server(config)
    server.run()