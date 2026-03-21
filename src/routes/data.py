from fastapi import FastAPI , APIRouter  , Depends , status , Request , UploadFile
from fastapi.responses import JSONResponse
from helpers.config import get_settings , settings
from controllers import DataController , ProjectController , ProcessController
from models import ResponseSignal
import logging 
import os 
import aiofiles 
from .schemas.data import ProcessRequest


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
    
    project_controller = ProjectController()
    project_dir = project_controller.get_project_dir(project_id = project_id)
    file_path , file_id = DataController().generate_filename(project_id=project_id , filename=uploaded_file.filename)
    
    try : 
        
        async with aiofiles.open(file_path , 'wb') as file : 
            while chunk := await uploaded_file.read(data_cont.app_settings.FILE_DEFAULT_CHUNK_SIZE) : 
                await file.write(chunk)
    except Exception as e : 
         
        logger.error(f"Error while uploading file {e}") 
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST , 
            content=ResponseSignal.FILE_UPLOAD_FAILED.value
            )
        
            
    
    return JSONResponse(
        content = {
            'content' : ResponseSignal.FILE_UPLOAD_SUCCESS.value , 
            'file_id' : file_id
        }
    )
    
    
    
    
    
@data_router.post("/process/{project_id}")
async def process_endpooint(project_id : str , process_request : ProcessRequest):
    file_id = process_request.file_id
    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size    
    
    process_controller = ProcessController(project_id=project_id)
    
    file_content = process_controller.get_file_content(file_id)
    file_chunks = process_controller.process_file_content(
        file_id = file_id , 
        chunk_size=chunk_size , 
        overlap_size=overlap_size , 
        file_content=file_content
    )

    if not file_chunks or len(file_chunks) == 0 : 
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST , 
            content = {
                'signal' : ResponseSignal.PROCESSING_FAILED.value
            }
        )
        
        
    return JSONResponse(
        status_code = status.HTTP_200_OK , 
        content = {
            'signal' : ResponseSignal.PROCESSING_SUCCESS.value , 
            'documents' : [doc.dict() for doc in file_chunks]
        }
    )
     
    