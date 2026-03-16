from .BaseController import BaseController
from fastapi import UploadFile
from  models.enums import ResponseSignal





class DataController(BaseController) : 
    def __init__(self):
        super().__init__() 
        self.scale_size = 1024 * 1024
        
    def validate_uploaded_file(self , file : UploadFile) : 
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES : 
            return False , ResponseSignal.FILE_NOT_ALLOWED_TYPES.value 
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.scale_size : 
            return False , ResponseSignal.FILE_SIZE_EXCEED.value
        
        return True , ResponseSignal.FILE_VALIDATE_SUCCESS.value