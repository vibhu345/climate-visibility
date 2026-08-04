# in this file till now we have data both train and test and both the data are scalled so we will now
# start model training
#Remember our data ie train and test data are in array form
import os,sys
from src.logger import logging
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
class ModelTrainingConfig:
    trained_model_path=os.path.join("artifacts","file containing trained model path")
class ModelTraining :
    def __init__(self):
        self.trained_model_path=ModelTrainingConfig()
    def evaluation_metrics(self,actual,predict):
        rmse=np.sqrt(mean_squared_error(actual,predict))
        mae=mean_absolute_error(actual,predict)
        r2=r2_score(actual,predict)


    logging.info("we are starting with train test split")
    def initiate_model_training(train_data,test_data):
        try:
            x_train,x_test,y_train,y_test=(train_data[:,:,-1],train_data[:,-1],test_data[:,:,-1],test_data[:,-1])
            models = {
                    "Random Forest": RandomForestRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Gradient Boosting": GradientBoostingRegressor(),
                    "Linear Regression": LinearRegression(),
                    "XGBRegressor": XGBRegressor(),
                    "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                    "AdaBoost Regressor": AdaBoostRegressor(),
                }
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }
            model_report:dict=evaluate_models(x_train,y_train,x_test,y_test)
            # to get the best model score from dict
            logging.info("Model report",model_report)
            logging.info(model_report.values())
            logging.info(model_report.keys())
            best_model_score=max(sorted(model_report.values()))
            logging.info(model_report.values().index(best_model_score))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            print("This is the best model")
            print(best_model_name)
            model_names=list(params.keys())
        except Exception as e:
            raise CustomException(e,sys)