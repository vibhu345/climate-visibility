# yeh file banayi gyi hai folder creation ke kaam ko asaan karne ke liye
import os # use karte hai taki current folder mein subfolder vagerah bana sake
from pathlib import Path # hum jis folder mein kam kar rahe hai uss folder mein se agar kisis subfloder ya file ka relative path chahiye tab yeh function use hota hai
import logging
logging.basicConfig(level=logging.INFO)
project_name="Project for practice"
list_of_files=[
    f"src/components/__init__.py", # src ke andar ek components naam ka folder banao aur usse pakage bana do
    f"src/components/data_ingestion.py", # src ke andar jo components naam ka folder hai uske andar data_ingestion naam ki ek file bana do
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/components/model_evaluation.py",
    f"src/pipelines/__init__.py", # src ke andar ek pipelines naam ka folder banao aur usse pakage bana do
    f"src/pipelines/training_pipeline.py", # src ke andar jo pipelines naam ka folder hai uske andar training_pipeline naam ki ek file bana do
    f"src/pipelines/prediction_pipeline.py",
    f"src/exception.py", # src ke andar exception naam ki file
    f"src/logger.py", # src folder ke andar logger naam ki file bana do
    f"src/utils.py", #src folder ke andar utils naam ki file bana do
    "requirements.txt",
    "setup.py",
    "app.py"

]
for i in list_of_files:
    filepath=Path(i) # yeh line nhi samjha
    filedir,filename=os.path.split(filepath) # uper se jo path mila hai uske do tukde kiye 
    if filedir != "": # if filedir has a name assign to it
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directry:{filedir} for the file {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)): # if a file of filepath do not exists or if a file of filepath exists but its size is zero that is nothing is written in that file then we create a file
        with open(filepath,"w") as f:
            pass
            logging.info(f"created an empty file,{filepath}")
    else: # else we will not create file
        logging.info(f"File already exist,{filename}")




