from fastapi import FastAPI
from books_store.routers import router

app = FastAPI()
app.include_router(router)

