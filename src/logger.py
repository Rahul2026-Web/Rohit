import logging
import os
from datetime import datetime

# Create log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create full log directory path
log_dir = os.path.join(os.getcwd(), "logs" ,LOG_FILE)
os.makedirs(log_dir, exist_ok=True)

# Create full log file path
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



    


