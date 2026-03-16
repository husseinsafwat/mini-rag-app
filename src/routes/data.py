from fastapi import FastAPI , APIRouter  , Depends , status , Request , UploadFile
from fastapi.responses import JSONResponse
from helpers.config import get_settings , settings
from controllers import DataController
import logging 

logger = logging.getLogger("uvicorn.error")

data_router = APIRouter(
    prefix = "/api/v1/data" , tags = ['api_v1' , 'data']
)



@data_router.post("/upload/{project_id}")
async def upload_file(project_id : str , uploaded_file : UploadFile , 
                      app_settings : settings = Depends(get_settings) ) :
    
    data_cont = DataController()
    valid , signal  = data_cont.validate_uploaded_file(file = uploaded_file)
    
    if not valid : 
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST , 
            content=signal
        )
    
    return JSONResponse(
        status_code=status.HTTP_200_OK , 
        content = signal
    )
    
    
    
    
    
    
    
     
    