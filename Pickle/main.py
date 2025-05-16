from fastapi import FastAPI
from routers import search, summary, detail

app = FastAPI()

app.include_router(search.router)
app.include_router(summary.router)
app.include_router(detail.router)