#data ingestion ka maksad hai ki hume training data,testing data ka path de. hum input mein denge data
# file(csv),path jaha par training data ko save karna hai aur path jaha par testing data ko save karna hai
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
@dataclass # so that you dont need to add constructor and write again and again self.
class DataIngestionConfig:
    # abhi hum path define kar rahe hai yaha par ki hamara data jis file mein hoga uss file ka path kaisa hoga
    train_data_path : str =os.path.join("artifacts","train_data.csv") # yani ki artifacts folder hum banayenge abji aage jiske andar ek file banao train_data.csv naam se aur us file ka path train_data_path mein store kardo(in the form of string)
    test_data_path : str=os.path.join("artifacts","test_data.csv") # yani ki artifacts folder hum banayenge abji aage jiske andar ek file banao test_data.csv naam se aur us file ka path test_data_path mein store kardo (in the form of string)
    raw_data_path : str=os.path.join("artifacts","raw_data.csv") # yani ki artifacts folder hum banayenge abji aage jiske andar ek file banao raw_data.csv naam se aur us file ka path raw_data_path mein store kardo (in the form of string)

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("we have started data ingestion")
        try:
            df=pd.read_csv("data.csv")
            logging.info("we have read the raw data")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # os.path.dirname kya karta hai,yeh function aapne joh path isme dala hai (train_data_path) uss path mein folder ka naam le leta hai ie artifacts nikal lega aur os.make.dirs ko dedega aur os.makedirs ek directry bana dega artifacts ke naam se 
            logging.info("storing the raw data into artifacts folder inro raw_data_file") 
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # # raw data to csv format mein save kar rahe hai in raw_data_path,index=False means sno wala column nhi aayega aur header=True means columns ka naam bhi save hoga
            logging.info("starting with train_test_split ie splitting the raw data into training data and testing data")
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=1)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("train test splitting is done")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    try:
        obj=DataIngestion()
        train_data_set_path,test_data_set_path=obj.initiate_data_ingestion()
        datatransformation=DataTransformation()
        datatransformation.initiate_data_transformation(train_data_set_path,test_data_set_path)
    except Exception as e:
        raise CustomException(e,sys)



