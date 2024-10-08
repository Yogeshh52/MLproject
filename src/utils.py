import os 
import sys
import numpy as np
import pandas as pd
import dill
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as f:
            dill.dump(obj,f)
            
    except Exception as e:
        raise CustomException(e,sys)