from .ProjectController import ProjectController
from .BaseController import BaseController
import os 
from models.enums import ProcessEnum
from langchain_community.document_loaders import TextLoader , PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class ProcessController(BaseController) : 
    def __init__(self , project_id):
        super().__init__()
        self.project_id = project_id 
        self.project_path = ProjectController().get_project_dir(project_id = self.project_id)
        
        
    def get_file_extension(self , file_id) :
        root , extension = os.path.splitext(file_id)
        return extension
    
    def get_file_loader(self , file_id ) : 
        file_ext = self.get_file_extension(file_id = file_id)
        file_path = os.path.join(self.project_path , file_id)
        
        
        if file_ext == ProcessEnum.TXT.value : 
            return TextLoader(os.path.abspath(os.path.normpath(file_path)), encodings = 'utf-8')
        
        if file_ext == ProcessEnum.PDF.value : 
            return PyMuPDFLoader(os.path.abspath(os.path.normpath(file_path)))
        
        return None
    
    
    def get_file_content(self , file_id) : 
        
        loader = self.get_file_loader(file_id) 
        return loader.load()
    
    
    def process_file_content(self , file_content:list , file_id:str , chunk_size:int=100 , overlap_size:int=30 ) :
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size , 
            chunk_overlap = overlap_size , 
            length_function = len )
         
         
        file_content_texts = [
             rec.page_content
             for rec in file_content 
         ]
        
        
        file_content_metadeta = [
            rec.metadata
            for rec in file_content
        ]
        
        chunks = text_splitter.create_documents(
            file_content_texts , 
            metadatas = file_content_metadeta
        )
         
         
        return chunks
         
        