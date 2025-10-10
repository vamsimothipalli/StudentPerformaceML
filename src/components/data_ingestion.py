import logging
import sys
import os
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
@dataclass
class DataIngestionConfig:
  train_data_path: str=os.path.join('artifacts',"train.csv")
  test_data_path: str = os.path.join('artifacts', "test.csv")
  raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
      self.config = DataIngestionConfig()
    def initiate_data_ingestion(self):
      logging.info("Entered the data ingestion method")
      try:
        df = pd.read_csv('C:/Users/18045/.cache/kagglehub/datasets/lainguyn123/student-performance-factors/versions/9/StudentPerformanceFactors.csv')
        logging.info("Read the dataset as dataframe")
        os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
        df.to_csv(self.config.raw_data_path, index=False,header=True)
        logging.info("Train test split initiated")
        train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
        train_set.to_csv(self.config.train_data_path, index=False,header=True)
        test_set.to_csv(self.config.test_data_path, index=False,header=True)
        logging.info("Ingestion complete")
        return(
          self.config.train_data_path,self.config.test_data_path
        )
      except Exception as e:
        raise CustomException(e,sys)


def error_message_detail(error,error_detail:sys):
    exc_type, exc_value, exc_traceback = error_detail.exc_info()
    file_name=exc_traceback.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_traceback.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
  def __init__(self,error_message, error_detail:sys):
    super().__init__(error_message, error_detail)
    self.error_message = error_message_detail(error_message, error_detail=error_detail)
  def __str__(self):
    return self.error_message

if __name__ == '__main__':
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)


