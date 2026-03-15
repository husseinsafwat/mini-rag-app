from fastapi import FastAPI , APIRouter 
import os 

base_router = APIRouter(
    prefix = "/api/v1" , tags = ['api_v1']
)


@base_router.get("/")
async def Welcome() : 
    app_name = os.getenv("APP_NAME")
    version = os.getenv("VERSION")
    return {'APP_NAME' : app_name  , 
            "VERSION" : version}