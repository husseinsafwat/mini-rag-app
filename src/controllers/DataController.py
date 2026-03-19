from .BaseController  import BaseController  
from .ProjectController import ProjectController
from fastapi import UploadFile
from  models.enums import ResponseSignal
import os  
import re 

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
    
    
    
    def generate_filename(self , project_id : str , filename : str) -> str : 
        
        random_file_name = self.generate_random_string()
        project_object = ProjectController()
        project_path = project_object.get_project_dir(project_id=project_id)
        
        cleaned_filename = self.get_clean_file_name(filename=filename)
        
        new_file_name = os.path.join(project_path , random_file_name+"_"+cleaned_filename)
        
        while os.path.exists(new_file_name) : 
            random_file_name = self.generate_random_string()
            new_file_name = os.path.join(project_path , random_file_name+"_"+cleaned_filename)
            
        return new_file_name , random_file_name+"_"+cleaned_filename
        
    def get_clean_file_name(self , filename : str ) -> str : 
        
        # Remove any special characters except . and _
        cleaned_file_name = re.sub(r'[^\w.]' , '' , filename.strip())
        
        # Replace any space with _
        cleaned_file_name = cleaned_file_name.replace(" " , "_")
        
        return cleaned_file_name
    
        
    
    
        