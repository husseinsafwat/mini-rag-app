from fastapi import FastAPI , APIRouter  , Depends
from helpers.config import get_settings , settings
base_router = APIRouter(
    prefix = "/api/v1" , tags = ['api_v1']
)


@base_router.get("/")
async def Welcome(app_settings : settings = Depends(get_settings)) : 
    app_settings = get_settings()
    app_name = app_settings.APP_NAME 
    version = app_settings.VERSION
    return {'APP_NAME' : app_name  , 
            "VERSION" : version}