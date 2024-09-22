import uvicorn
from fastapi import FastAPI

from app.api.endpoints.user import router as user_auth_router
from app.api.endpoints.currency import router as currency_router
from app.database.db import init_db

app = FastAPI()
app.include_router(user_auth_router)
app.include_router(currency_router)


@app.on_event("startup")
async def startup_event():
    await init_db()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
