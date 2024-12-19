from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database import init_db
from routers import book_router, author_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(book_router.router, prefix="/books", tags=["Books"])
app.include_router(author_router.router, prefix="/authors", tags=["Authors"])


@app.get("/")
async def read_root():
    return {"message": "Library Management API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
