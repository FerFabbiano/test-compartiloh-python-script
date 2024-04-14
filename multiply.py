import os
import logging
import time

# Get the absolute path to the current directory
current_dir = os.path.abspath(os.path.dirname(__file__))

# Specify the log file name and create the absolute path
log_file_path = os.path.join(current_dir, 'results', 'app.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

logging.info("Hello World!")
i = 0
while i < 100:
  i += 1
  
logging.info("Finished loop")
