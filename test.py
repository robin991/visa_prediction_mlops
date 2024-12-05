from us_visa.logger import logging
from  us_visa.exception import USVisaException
logging.info("check this")
import os
try: 
    dotenv_path = os.path.join(os.path.dirname(__file__), "us_visa\environment_var", ".env")
    print(dotenv_path)

except USVisaException as e:
    logging.error(e)