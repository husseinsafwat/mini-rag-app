from enum import Enum




class ResponseSignal(Enum) : 
    FILE_VALIDATE_SUCCESS = "file_validates_successfully"
    FILE_NOT_ALLOWED_TYPES = "file_type_not_allowed"
    FILE_SIZE_EXCEED = 'file_size_exceeded'
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_FAILED = 'processing_faild'
    PROCESSING_SUCCESS = 'processing_success'
    