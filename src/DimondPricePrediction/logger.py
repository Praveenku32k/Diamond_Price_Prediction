import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs") # it will create new folder called logs ,it creats the path.

os.makedirs(log_path,exist_ok=True) # creating the directory for the log files ..

LOG_FILEPATH=os.path.join(log_path,LOG_FILE) # joining the log_path and Log_file inside LOG_FILEPATH.


logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)
# TIME , LINENUMBER , NAME, ....FOR ABOVE CELL

if __name__ == '__main__':
    logging.info("here again i am tesitng")