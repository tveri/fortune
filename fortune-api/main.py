import uvicorn
from fastapi import FastAPI, Response
from fastapi.routing import APIRouter

import settings
from api.handlers import user_router


app = FastAPI()

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(main_api_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)