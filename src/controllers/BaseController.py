from helpers.config import settings , get_settings 
import os 
import random 
import string


class BaseController : 
    def __init__(self) : 
        self.app_settings = get_settings()
    