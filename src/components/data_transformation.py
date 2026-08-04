import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from sklearn.preprocessing import StandardScaler
from src.exception import CustomException
import sys
import pickle
from sklearn.compose import ColumnTransformer
class DataTransformation:

    # VWTI,SWTI,CWTI,EI
    def scaler(self):
        try:
            num_cols=["DRYBULBTEMPF","WETBULBTEMPF","DewPointTempF","RelativeHumidity","WindSpeed","WindDirection","StationPressure","SeaLevelPressure","Precip"]
            preprocessor=ColumnTransformer([
                ("numerical columns",StandardScaler(),num_cols)])
            return (preprocessor,num_cols)
        except Exception as e:
            raise CustomException(e,sys)
    

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            logging.info("entered into DataTransformation class")
            preprocessor_path=os.path.join("artifacts","proprocessor_saved.pkl")
            logging.info("reading the data from the path returned by data ingestion class")
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            logging.info("separating the data into x and y")
            x_train=train_data.drop("VISIBILITY",axis=1)
            x_test=test_data.drop("VISIBILITY",axis=1)
            y_train=train_data["VISIBILITY"]
            y_test=test_data["VISIBILITY"]
            logging.info("starting with scalling and encoding")
            preprocessor_obj,num_cols=self.scaler()
            x_train_scalled=preprocessor_obj.fit_transform(x_train)
            x_test_scalled=preprocessor_obj.transform(x_test)
            x_train_df=pd.DataFrame(x_train_scalled,columns=num_cols)
            x_test_df=pd.DataFrame(x_test_scalled,columns=num_cols)
            logging.info("scalling ho gyi hai aur now saving the preprocessor object")
            os.makedirs(os.path.dirname(preprocessor_path),exist_ok=True)
            with open (preprocessor_path,"wb" )as file_obj:
                pickle.dump(preprocessor_obj,file_obj)
            logging.info("exiting the DataTransformation class and this class will return me train and test dataframes which are scalled")
            return (x_train_df,x_test_df,y_train,y_test,preprocessor_path)
        except Exception as e:
            raise CustomException(e,sys)





    