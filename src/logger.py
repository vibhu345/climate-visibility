import logging
import os
from datetime import datetime
# creating a LOG File
LOG_File= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# defining the directry path (pointing to the "logs" folder only)
log_dir=os.path.join(os.getcwd(),"LOGGGGGGS")
# crete the directry safely if it does not exists
os.makedirs(log_dir,exist_ok=True)
# combine the directry and filename for the final path
LOG_FILE_PATH=os.path.join(log_dir,LOG_File)

logging.basicConfig(
filename=LOG_FILE_PATH,
level=logging.INFO,
format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
